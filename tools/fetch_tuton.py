#!/usr/bin/env python3
"""
Fetcher soal Tuton UT via Moodle REST API
Penggunaan: python3 fetch_tuton.py <NIM> <PASSWORD> [nomor_modul]
Contoh    : python3 fetch_tuton.py 123456789 MyPass123 7
"""

import sys
import json
import re
import os
import time
from pathlib import Path

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Jalankan: pip3 install requests beautifulsoup4")
    sys.exit(1)

# ─── Config ──────────────────────────────────────────────────────────────────
BASE_URL  = "https://elearning.ut.ac.id"
TOKEN_URL = f"{BASE_URL}/login/token.php"
API_URL   = f"{BASE_URL}/webservice/rest/server.php"
SERVICE   = "moodle_mobile_app"
OUT_DIR   = Path(__file__).parent / "soal_output"
OUT_DIR.mkdir(exist_ok=True)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
    ),
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8",
}


def strip_html(html_text: str) -> str:
    """Hapus tag HTML, kembalikan teks bersih."""
    if not html_text:
        return ""
    soup = BeautifulSoup(html_text, "html.parser")
    return soup.get_text(separator="\n").strip()


def api_call(session, token: str, function: str, **params) -> dict:
    """Panggil Moodle REST API."""
    payload = {
        "wstoken": token,
        "wsfunction": function,
        "moodlewsrestformat": "json",
        **params,
    }
    r = session.get(API_URL, params=payload, timeout=30)
    r.raise_for_status()
    data = r.json()
    if isinstance(data, dict) and "exception" in data:
        raise RuntimeError(f"Moodle API error [{function}]: {data.get('message', data)}")
    return data


# ─── Step 1: Autentikasi ─────────────────────────────────────────────────────
def get_token(session, nim: str, password: str) -> str:
    print("  [1/5] Autentikasi ke elearning.ut.ac.id ...")
    r = session.post(TOKEN_URL, data={
        "username": nim,
        "password": password,
        "service": SERVICE,
    }, timeout=30)
    r.raise_for_status()
    data = r.json()
    if "token" not in data:
        msg = data.get("error") or data.get("message") or str(data)
        raise RuntimeError(f"Login gagal: {msg}")
    print(f"  => Token diperoleh.")
    return data["token"]


# ─── Step 2: Info user + courses ─────────────────────────────────────────────
def get_courses(session, token: str) -> tuple[int, list]:
    print("  [2/5] Mengambil daftar matkul ...")
    site_info = api_call(session, token, "core_webservice_get_site_info")
    user_id   = site_info["userid"]
    print(f"  => Login sebagai: {site_info.get('fullname', 'N/A')} (id={user_id})")

    courses = api_call(session, token, "core_enrol_get_users_courses", userid=user_id)
    print(f"  => {len(courses)} matkul ditemukan:")
    for c in courses:
        print(f"     • [{c['id']}] {c['fullname']}")
    return user_id, courses


# ─── Step 3: Isi course (sections/modul) ─────────────────────────────────────
def get_course_contents(session, token: str, course_id: int) -> list:
    return api_call(session, token, "core_course_get_contents", courseid=course_id)


# ─── Step 4: Forum diskusi ────────────────────────────────────────────────────
def get_forum_questions(session, token: str, forum_id: int, course_name: str,
                        modul_num: int) -> list:
    """Ambil pertanyaan diskusi dari forum ID tertentu."""
    try:
        discussions = api_call(
            session, token,
            "mod_forum_get_forum_discussions",
            forumid=forum_id, sortby="timemodified", sortdirection="DESC",
            page=0, perpage=50,
        )
        posts = discussions.get("discussions", discussions if isinstance(discussions, list) else [])
    except RuntimeError:
        return []

    results = []
    for d in posts:
        msg = strip_html(d.get("message", ""))
        name = d.get("name", "")
        results.append({
            "type": "diskusi",
            "judul": name,
            "soal": msg,
            "penulis": d.get("userfullname", ""),
        })
    return results


# ─── Step 5: Tugas (assignment) ───────────────────────────────────────────────
def get_assignment_questions(session, token: str, course_id: int, assign_ids: list) -> list:
    """Ambil detail tugas."""
    try:
        data = api_call(
            session, token,
            "mod_assign_get_assignments",
            courseids=[course_id],
        )
    except RuntimeError:
        return []

    results = []
    for course in data.get("courses", []):
        for assign in course.get("assignments", []):
            if assign_ids and assign["cmid"] not in assign_ids:
                continue
            soal = strip_html(assign.get("intro", ""))
            results.append({
                "type": "tugas",
                "judul": assign.get("name", ""),
                "soal": soal,
                "deadline": assign.get("duedate", 0),
            })
    return results


# ─── Main ─────────────────────────────────────────────────────────────────────
def main():
    if len(sys.argv) < 3:
        print("Penggunaan: python3 fetch_tuton.py <NIM> <PASSWORD> [nomor_modul]")
        print("Contoh    : python3 fetch_tuton.py 12345678 MyPass123 7")
        sys.exit(1)

    nim       = sys.argv[1]
    password  = sys.argv[2]
    target_modul = int(sys.argv[3]) if len(sys.argv) > 3 else 7

    print(f"\n{'='*60}")
    print(f"  Fetcher Soal Tuton UT — Modul {target_modul}")
    print(f"{'='*60}\n")

    session = requests.Session()
    session.headers.update(HEADERS)

    # Auth
    try:
        token = get_token(session, nim, password)
    except Exception as e:
        print(f"\nGAGAL: {e}")
        print("\nKemungkinan penyebab:")
        print("  1. NIM atau password salah")
        print("  2. Server UT memblokir akses dari IP luar Indonesia")
        print("  3. Layanan webservice Moodle dinonaktifkan UT")
        print("\nSolusi: Copy-paste teks soal dari browser kamu ke sini.")
        sys.exit(1)

    # Courses
    try:
        user_id, courses = get_courses(session, token)
    except Exception as e:
        print(f"GAGAL ambil courses: {e}")
        sys.exit(1)

    print(f"\n  [3/5] Mengambil isi modul {target_modul} per matkul ...")

    semua_soal = {}

    for course in courses:
        cid   = course["id"]
        cname = course["fullname"]
        short = course.get("shortname", cname[:20])
        print(f"\n  -- {cname} --")

        try:
            sections = get_course_contents(session, token, cid)
        except Exception as e:
            print(f"     Lewat (error: {e})")
            continue

        # Cari section yang berisi "modul 7" atau index ke-7
        target_section = None
        for sec in sections:
            sec_name = sec.get("name", "").lower()
            # Coba cocokkan "modul 7", "minggu 7", "week 7", "7", atau index
            if (f"modul {target_modul}" in sec_name or
                f"minggu {target_modul}" in sec_name or
                f"week {target_modul}" in sec_name or
                sec_name == str(target_modul) or
                sec.get("section") == target_modul):
                target_section = sec
                break

        # Fallback: ambil berdasarkan urutan
        if not target_section and len(sections) >= target_modul:
            target_section = sections[target_modul - 1]

        if not target_section:
            print(f"     Modul {target_modul} tidak ditemukan.")
            continue

        print(f"     Section ditemukan: '{target_section.get('name', '-')}'")

        forum_ids  = []
        assign_ids = []

        for mod in target_section.get("modules", []):
            mtype = mod.get("modname", "")
            mid   = mod.get("instance", 0)
            mname = mod.get("name", "")
            if mtype == "forum":
                forum_ids.append((mid, mname))
                print(f"     [Forum] {mname} (id={mid})")
            elif mtype == "assign":
                assign_ids.append(mod.get("id", 0))
                print(f"     [Tugas] {mname} (id={mid})")

        soal_matkul = []

        for fid, fname in forum_ids:
            qs = get_forum_questions(session, token, fid, cname, target_modul)
            soal_matkul.extend(qs)

        if assign_ids:
            qs = get_assignment_questions(session, token, cid, assign_ids)
            soal_matkul.extend(qs)

        semua_soal[short] = {
            "nama_lengkap": cname,
            "modul": target_modul,
            "soal": soal_matkul,
        }

        # Simpan ke file teks
        out_file = OUT_DIR / f"modul{target_modul}_{short.replace(' ', '_')}.txt"
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(f"MATKUL  : {cname}\n")
            f.write(f"MODUL   : {target_modul}\n")
            f.write("=" * 60 + "\n\n")
            if soal_matkul:
                for i, s in enumerate(soal_matkul, 1):
                    f.write(f"[{s['type'].upper()} {i}]\n")
                    f.write(f"Judul   : {s['judul']}\n")
                    f.write(f"Soal    :\n{s['soal']}\n")
                    f.write("-" * 40 + "\n\n")
            else:
                f.write("(Tidak ada soal ditemukan di section ini)\n")
        print(f"     => {len(soal_matkul)} soal disimpan ke {out_file.name}")

    # Simpan JSON lengkap
    json_out = OUT_DIR / f"semua_soal_modul{target_modul}.json"
    with open(json_out, "w", encoding="utf-8") as f:
        json.dump(semua_soal, f, ensure_ascii=False, indent=2)

    print(f"\n  [5/5] Selesai!")
    print(f"  Output tersimpan di: {OUT_DIR}/")
    print(f"  File JSON  : {json_out.name}")
    print(f"\n{'='*60}")
    print("  RINGKASAN SOAL")
    print(f"{'='*60}")
    for short, data in semua_soal.items():
        soal_list = data["soal"]
        print(f"\n  [{short}] {data['nama_lengkap']}")
        if soal_list:
            for s in soal_list:
                print(f"    {s['type'].upper()}: {s['judul']}")
                preview = s['soal'][:200].replace('\n', ' ')
                print(f"    => {preview}...")
        else:
            print("    (tidak ada soal terdeteksi)")

    # Hapus credentials dari memori
    del nim, password
    print(f"\n  Credentials dihapus dari memori.")


if __name__ == "__main__":
    main()
