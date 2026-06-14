#!/usr/bin/env python3
"""Generator template jawaban UT S1 Hukum - 8 Matkul Semester 1-2"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "pdf")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ─── Warna tema ───────────────────────────────────────────────────────────────
BIRU_UT   = colors.HexColor("#003087")
EMAS_UT   = colors.HexColor("#D4A017")
ABU_MUDA  = colors.HexColor("#F4F4F4")
ABU_BORDER= colors.HexColor("#CCCCCC")

# ─── Styles ───────────────────────────────────────────────────────────────────
def buat_styles():
    styles = getSampleStyleSheet()

    styles.add(ParagraphStyle(
        "JudulCover", fontName="Helvetica-Bold", fontSize=20,
        textColor=BIRU_UT, alignment=TA_CENTER, spaceAfter=8, leading=26
    ))
    styles.add(ParagraphStyle(
        "SubjudulCover", fontName="Helvetica", fontSize=13,
        textColor=colors.white, alignment=TA_CENTER, spaceAfter=4, leading=18
    ))
    styles.add(ParagraphStyle(
        "HeaderModul", fontName="Helvetica-Bold", fontSize=13,
        textColor=colors.white, alignment=TA_LEFT, spaceAfter=0, leading=18,
        leftIndent=6
    ))
    styles.add(ParagraphStyle(
        "SubHeader", fontName="Helvetica-Bold", fontSize=11,
        textColor=BIRU_UT, spaceAfter=4, spaceBefore=10, leading=14
    ))
    styles.add(ParagraphStyle(
        "Label", fontName="Helvetica-Bold", fontSize=9,
        textColor=colors.HexColor("#444444"), spaceAfter=2, leading=12
    ))
    styles.add(ParagraphStyle(
        "Body", fontName="Helvetica", fontSize=9,
        textColor=colors.black, spaceAfter=4, leading=13, alignment=TA_JUSTIFY
    ))
    styles.add(ParagraphStyle(
        "IsiTemplate", fontName="Helvetica", fontSize=9,
        textColor=colors.HexColor("#333333"), spaceAfter=3, leading=13,
        leftIndent=8, alignment=TA_JUSTIFY
    ))
    styles.add(ParagraphStyle(
        "Catatan", fontName="Helvetica-Oblique", fontSize=8,
        textColor=colors.HexColor("#666666"), spaceAfter=2, leading=11
    ))
    styles.add(ParagraphStyle(
        "KataKunci", fontName="Helvetica", fontSize=8,
        textColor=colors.HexColor("#555555"), spaceAfter=2, leading=11,
        leftIndent=8
    ))
    return styles


def header_modul(nomor, topik, styles):
    """Kotak header biru untuk judul modul."""
    tabel = Table(
        [[Paragraph(f"MODUL {nomor}: {topik.upper()}", styles["HeaderModul"])]],
        colWidths=[17.5*cm]
    )
    tabel.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), BIRU_UT),
        ("TOPPADDING",    (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 6),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
        ("RIGHTPADDING",  (0,0), (-1,-1), 8),
        ("ROUNDEDCORNERS", [4]),
    ]))
    return tabel


def kotak_isian(label, baris=3, styles=None):
    """Kotak abu-abu untuk isian jawaban mahasiswa."""
    garis = ("_" * 80 + "\n") * baris
    tabel = Table(
        [[Paragraph(f"<b>{label}</b>", styles["Label"]),
          Paragraph(garis, styles["Catatan"])]],
        colWidths=[4*cm, 13.5*cm]
    )
    tabel.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), ABU_MUDA),
        ("BOX",           (0,0), (-1,-1), 0.5, ABU_BORDER),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 6),
        ("RIGHTPADDING",  (0,0), (-1,-1), 6),
        ("VALIGN",        (0,0), (-1,-1), "TOP"),
    ]))
    return tabel


def blok_template_diskusi(nomor_modul, pertanyaan_contoh, kata_kunci, panduan, styles):
    """Blok lengkap template diskusi per modul."""
    elems = []

    # Sub-header diskusi
    elems.append(Spacer(1, 0.3*cm))
    tbl_disk = Table(
        [[Paragraph(f"  DISKUSI MINGGU {nomor_modul}", styles["Label"])]],
        colWidths=[17.5*cm]
    )
    tbl_disk.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), EMAS_UT),
        ("TOPPADDING",    (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
    ]))
    elems.append(tbl_disk)
    elems.append(Spacer(1, 0.2*cm))

    # Contoh pertanyaan diskusi
    elems.append(Paragraph("Contoh Pertanyaan Diskusi:", styles["Label"]))
    elems.append(Paragraph(f'<i>"{pertanyaan_contoh}"</i>', styles["IsiTemplate"]))
    elems.append(Spacer(1, 0.2*cm))

    # Kata kunci
    elems.append(Paragraph("Kata Kunci yang Harus Muncul:", styles["Label"]))
    for kk in kata_kunci:
        elems.append(Paragraph(f"• {kk}", styles["KataKunci"]))
    elems.append(Spacer(1, 0.2*cm))

    # Template jawaban
    elems.append(Paragraph("TEMPLATE JAWABAN (isi dengan versimu sendiri):", styles["SubHeader"]))

    elems.append(Paragraph("Pembuka:", styles["Label"]))
    elems.append(kotak_isian("Salam & intro", 2, styles))
    elems.append(Spacer(1, 0.15*cm))

    for i, panduan_par in enumerate(panduan, 1):
        elems.append(Paragraph(f"Paragraf {i} — {panduan_par}:", styles["Label"]))
        elems.append(kotak_isian("Isi", 3, styles))
        elems.append(Spacer(1, 0.15*cm))

    elems.append(Paragraph("Kesimpulan:", styles["Label"]))
    elems.append(kotak_isian("Simpulan", 2, styles))
    elems.append(Spacer(1, 0.15*cm))

    elems.append(Paragraph("Referensi (Modul UT / Buku / UU):", styles["Label"]))
    elems.append(kotak_isian("Sumber", 2, styles))

    return elems


def blok_tugas(nomor_tugas, deskripsi, instruksi_poin, styles):
    """Blok template tugas (ada 3 tugas per semester)."""
    elems = []
    elems.append(Spacer(1, 0.4*cm))
    tbl_t = Table(
        [[Paragraph(f"  TUGAS {nomor_tugas} (Cakupan Modul {(nomor_tugas-1)*3+1}-{nomor_tugas*3})",
                    styles["Label"])]],
        colWidths=[17.5*cm]
    )
    tbl_t.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#1a5276")),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
    ]))
    elems.append(tbl_t)
    elems.append(Spacer(1, 0.2*cm))
    elems.append(Paragraph(f"Gambaran Tugas: {deskripsi}", styles["Body"]))
    elems.append(Spacer(1, 0.2*cm))
    for i, instruksi in enumerate(instruksi_poin, 1):
        elems.append(Paragraph(f"<b>Poin {i}:</b> {instruksi}", styles["Label"]))
        elems.append(kotak_isian("Jawaban", 4, styles))
        elems.append(Spacer(1, 0.2*cm))
    elems.append(Paragraph("Referensi & Daftar Pustaka:", styles["Label"]))
    elems.append(kotak_isian("Sumber", 3, styles))
    return elems


def halaman_cover(nama_matkul, kode_matkul, deskripsi, styles):
    """Halaman cover per matkul."""
    elems = []
    elems.append(Spacer(1, 1.5*cm))

    # Banner header
    tbl_cover = Table(
        [[Paragraph("UNIVERSITAS TERBUKA", styles["SubjudulCover"])],
         [Paragraph("S1 ILMU HUKUM", styles["SubjudulCover"])]],
        colWidths=[17.5*cm]
    )
    tbl_cover.setStyle(TableStyle([
        ("BACKGROUND",    (0,0), (-1,-1), BIRU_UT),
        ("TOPPADDING",    (0,0), (-1,-1), 8),
        ("BOTTOMPADDING", (0,0), (-1,-1), 8),
        ("ALIGN",         (0,0), (-1,-1), "CENTER"),
    ]))
    elems.append(tbl_cover)
    elems.append(Spacer(1, 0.5*cm))

    elems.append(Paragraph("TEMPLATE JAWABAN DISKUSI & TUGAS", styles["JudulCover"]))
    elems.append(Spacer(1, 0.2*cm))

    tbl_nama = Table(
        [[Paragraph(nama_matkul.upper(), styles["JudulCover"])],
         [Paragraph(f"({kode_matkul})", ParagraphStyle("kode", fontName="Helvetica",
                    fontSize=11, textColor=colors.HexColor("#666666"),
                    alignment=TA_CENTER))]],
        colWidths=[17.5*cm]
    )
    tbl_nama.setStyle(TableStyle([
        ("BOX",           (0,0), (-1,-1), 1.5, EMAS_UT),
        ("TOPPADDING",    (0,0), (-1,-1), 10),
        ("BOTTOMPADDING", (0,0), (-1,-1), 10),
        ("BACKGROUND",    (0,0), (-1,-1), colors.HexColor("#F0F4FF")),
    ]))
    elems.append(tbl_nama)
    elems.append(Spacer(1, 0.5*cm))

    elems.append(Paragraph(deskripsi, ParagraphStyle(
        "desc", fontName="Helvetica", fontSize=10,
        textColor=colors.HexColor("#333333"), alignment=TA_CENTER, leading=15
    )))
    elems.append(Spacer(1, 1*cm))

    # Tabel identitas mahasiswa
    elems.append(Paragraph("IDENTITAS MAHASISWA", styles["SubHeader"]))
    data_id = [
        ["Nama Lengkap", ":"],
        ["NIM", ":"],
        ["Program Studi", ": S1 Ilmu Hukum"],
        ["Semester", ":"],
        ["UPBJJ / Kelas", ":"],
        ["Nama Tutor", ":"],
    ]
    tbl_id = Table(data_id, colWidths=[4.5*cm, 13*cm])
    tbl_id.setStyle(TableStyle([
        ("FONTNAME",      (0,0), (-1,-1), "Helvetica"),
        ("FONTSIZE",      (0,0), (-1,-1), 10),
        ("FONTNAME",      (0,0), (0,-1), "Helvetica-Bold"),
        ("BACKGROUND",    (0,0), (0,-1), ABU_MUDA),
        ("BOX",           (0,0), (-1,-1), 0.5, ABU_BORDER),
        ("INNERGRID",     (0,0), (-1,-1), 0.3, ABU_BORDER),
        ("TOPPADDING",    (0,0), (-1,-1), 5),
        ("BOTTOMPADDING", (0,0), (-1,-1), 5),
        ("LEFTPADDING",   (0,0), (-1,-1), 8),
    ]))
    elems.append(tbl_id)
    elems.append(Spacer(1, 0.5*cm))

    elems.append(Paragraph(
        "Petunjuk: Template ini berisi panduan mengerjakan diskusi dan tugas setiap modul. "
        "Isi bagian yang bertanda garis bawah dengan jawabanmu sendiri. "
        "Gunakan kata kunci yang tercantum sebagai acuan isi jawaban.",
        styles["Catatan"]
    ))
    elems.append(PageBreak())
    return elems


# ═══════════════════════════════════════════════════════════════════════════════
# DATA 8 MATKUL
# ═══════════════════════════════════════════════════════════════════════════════

MATKUL = [
    # ── 1. Pengantar Ilmu Hukum ─────────────────────────────────────────────
    {
        "nama": "Pengantar Ilmu Hukum",
        "kode": "HKUM4101",
        "deskripsi": (
            "Mata kuliah ini membahas konsep dasar hukum, tujuan hukum, sumber hukum, "
            "norma hukum, subjek dan objek hukum, serta aliran-aliran dalam ilmu hukum."
        ),
        "modul": [
            {
                "topik": "Pengertian dan Fungsi Hukum",
                "pertanyaan": (
                    "Jelaskan apa yang dimaksud dengan hukum menurut para ahli dan "
                    "bagaimana fungsi hukum dalam kehidupan bermasyarakat!"
                ),
                "kata_kunci": [
                    "Definisi hukum (Utrecht, Apeldoorn, Immanuel Kant)",
                    "Fungsi hukum: kepastian, keadilan, kemanfaatan",
                    "Hukum sebagai alat kontrol sosial",
                    "Hukum positif vs hukum alam",
                ],
                "panduan": ["Definisi hukum dari minimal 2 ahli", "Fungsi dan tujuan hukum"],
                "tugas": None,
            },
            {
                "topik": "Tujuan Hukum",
                "pertanyaan": (
                    "Teori tujuan hukum manakah yang paling relevan diterapkan di Indonesia? "
                    "Jelaskan alasannya!"
                ),
                "kata_kunci": [
                    "Teori keadilan (Aristoteles, Rawls)",
                    "Teori kepastian hukum (positivisme)",
                    "Teori kemanfaatan (utilitarianisme – Bentham)",
                    "Teori gabungan (Utrecht)",
                ],
                "panduan": ["Uraikan 3 teori tujuan hukum", "Relevansi di Indonesia"],
                "tugas": None,
            },
            {
                "topik": "Sumber Hukum",
                "pertanyaan": (
                    "Apa perbedaan sumber hukum materiil dan formil? Berikan contohnya!"
                ),
                "kata_kunci": [
                    "Sumber hukum materiil (agama, kesusilaan, kehendak masyarakat)",
                    "Sumber hukum formil (UU, kebiasaan, yurisprudensi, traktat, doktrin)",
                    "Hierarki peraturan perundang-undangan (UU No.12/2011)",
                    "Contoh konkret masing-masing sumber",
                ],
                "panduan": ["Definisi & perbedaan materiil-formil", "Contoh tiap sumber hukum formil"],
                "tugas": {
                    "nomor": 1,
                    "deskripsi": "Menganalisis konsep dasar hukum (Modul 1-3).",
                    "poin": [
                        "Jelaskan pengertian hukum dan tujuan hukum menurut minimal 3 ahli!",
                        "Uraikan sumber-sumber hukum formil yang berlaku di Indonesia beserta contohnya!",
                        "Bagaimana hubungan antara keadilan, kepastian, dan kemanfaatan dalam hukum Indonesia?",
                    ],
                },
            },
            {
                "topik": "Norma Hukum",
                "pertanyaan": (
                    "Apa yang membedakan norma hukum dengan norma sosial lainnya? "
                    "Mengapa hukum memiliki sanksi yang memaksa?"
                ),
                "kata_kunci": [
                    "Norma hukum vs norma agama, susila, kesopanan",
                    "Sifat memaksa (dwingend recht) dan mengatur (aanvullend recht)",
                    "Sanksi dan penegakan norma hukum",
                    "Hierarki norma (Stufenbau – Kelsen)",
                ],
                "panduan": ["Ciri khas norma hukum", "Perbandingan dengan norma lain"],
                "tugas": None,
            },
            {
                "topik": "Subjek dan Objek Hukum",
                "pertanyaan": (
                    "Siapa saja yang dapat menjadi subjek hukum? Jelaskan perbedaan "
                    "antara manusia dan badan hukum sebagai subjek hukum!"
                ),
                "kata_kunci": [
                    "Subjek hukum: manusia (persoon) dan badan hukum (rechtspersoon)",
                    "Kecakapan bertindak hukum (handelingsbevoegdheid)",
                    "Objek hukum: benda (zaak) – berwujud dan tidak berwujud",
                    "Badan hukum publik vs privat",
                ],
                "panduan": ["Pengertian subjek hukum", "Badan hukum dan syarat-syaratnya"],
                "tugas": None,
            },
            {
                "topik": "Hubungan dan Peristiwa Hukum",
                "pertanyaan": (
                    "Apa yang dimaksud dengan peristiwa hukum? Berikan contoh peristiwa "
                    "hukum yang terjadi dalam kehidupan sehari-hari!"
                ),
                "kata_kunci": [
                    "Peristiwa hukum: perbuatan hukum dan peristiwa hukum bukan perbuatan",
                    "Perbuatan hukum sepihak dan dua pihak",
                    "Akibat hukum (rechtsgevolg)",
                    "Hubungan hukum (rechtsbetrekking)",
                ],
                "panduan": ["Definisi peristiwa hukum", "Contoh nyata + akibat hukumnya"],
                "tugas": {
                    "nomor": 2,
                    "deskripsi": "Menganalisis norma, subjek-objek, dan peristiwa hukum (Modul 4-6).",
                    "poin": [
                        "Jelaskan perbedaan norma hukum dengan norma sosial lainnya!",
                        "Siapa saja yang termasuk subjek hukum? Berikan contoh badan hukum di Indonesia!",
                        "Uraikan 3 contoh peristiwa hukum beserta akibat hukum yang ditimbulkan!",
                    ],
                },
            },
            {
                "topik": "Sistematika Hukum",
                "pertanyaan": (
                    "Bagaimana sistematika pembagian hukum di Indonesia? "
                    "Jelaskan perbedaan hukum publik dan hukum privat!"
                ),
                "kata_kunci": [
                    "Hukum publik: hukum pidana, HTN, HAN, hukum internasional",
                    "Hukum privat: hukum perdata, hukum dagang",
                    "Hukum materiil vs hukum formil",
                    "Hukum tertulis vs tidak tertulis",
                ],
                "panduan": ["Klasifikasi hukum publik-privat", "Contoh cabang hukum masing-masing"],
                "tugas": None,
            },
            {
                "topik": "Aliran-Aliran Ilmu Hukum",
                "pertanyaan": (
                    "Jelaskan perbedaan antara aliran positivisme hukum dan aliran "
                    "hukum alam! Mana yang lebih relevan di Indonesia?"
                ),
                "kata_kunci": [
                    "Positivisme hukum (Austin, Kelsen) – hukum = perintah",
                    "Hukum alam (Grotius, Aquinas) – hukum abadi universal",
                    "Realisme hukum (Holmes) – law in action",
                    "Sociological jurisprudence (Pound)",
                ],
                "panduan": ["Uraian tiap aliran", "Kritik dan relevansi di Indonesia"],
                "tugas": None,
            },
            {
                "topik": "Interpretasi dan Penemuan Hukum",
                "pertanyaan": (
                    "Metode interpretasi hukum apa saja yang dikenal? Berikan contoh "
                    "penerapannya dalam putusan pengadilan Indonesia!"
                ),
                "kata_kunci": [
                    "Interpretasi gramatikal, sistematis, historis, teleologis",
                    "Interpretasi ekstensif dan restriktif",
                    "Konstruksi hukum: analogi, a contrario, penghalusan hukum",
                    "Penemuan hukum oleh hakim (rechtsvinding)",
                ],
                "panduan": ["Jenis-jenis interpretasi", "Contoh kasus + metode yang digunakan"],
                "tugas": {
                    "nomor": 3,
                    "deskripsi": "Menganalisis sistematika dan penemuan hukum (Modul 7-9).",
                    "poin": [
                        "Jelaskan pembagian sistematika hukum di Indonesia beserta contohnya!",
                        "Bandingkan aliran positivisme hukum dengan hukum alam!",
                        "Berikan contoh kasus di Indonesia di mana hakim menggunakan metode interpretasi tertentu!",
                    ],
                },
            },
        ],
    },

    # ── 2. Sistem Hukum Indonesia ───────────────────────────────────────────
    {
        "nama": "Sistem Hukum Indonesia",
        "kode": "HKUM4201",
        "deskripsi": (
            "Mata kuliah ini membahas sistem hukum yang berlaku di Indonesia, "
            "meliputi sumber hukum, lembaga peradilan, hukum perdata, pidana, dagang, "
            "agraria, dan hubungannya dengan hukum internasional."
        ),
        "modul": [
            {
                "topik": "Pengertian dan Ruang Lingkup Sistem Hukum Indonesia",
                "pertanyaan": (
                    "Jelaskan pengertian sistem hukum dan bagaimana karakteristik "
                    "sistem hukum Indonesia sebagai sistem hukum campuran!"
                ),
                "kata_kunci": [
                    "Sistem hukum: civil law, common law, hukum Islam, hukum adat",
                    "Sistem hukum campuran (mixed legal system) Indonesia",
                    "Pengaruh kolonial Belanda (civil law) dalam KUHPerdata dan KUHP",
                    "Pluralisme hukum di Indonesia",
                ],
                "panduan": ["Definisi sistem hukum", "Karakteristik campuran hukum Indonesia"],
                "tugas": None,
            },
            {
                "topik": "Sumber Hukum Indonesia",
                "pertanyaan": (
                    "Sebutkan dan jelaskan hierarki peraturan perundang-undangan "
                    "di Indonesia berdasarkan UU No. 12 Tahun 2011!"
                ),
                "kata_kunci": [
                    "Hierarki: UUD 1945, TAP MPR, UU/Perppu, PP, Perpres, Perda Prov, Perda Kab/Kota",
                    "Asas lex superior derogat legi inferiori",
                    "Asas lex specialis derogat legi generali",
                    "Asas lex posterior derogat legi priori",
                ],
                "panduan": ["Hierarki perundang-undangan", "Asas-asas pemberlakuan peraturan"],
                "tugas": None,
            },
            {
                "topik": "Tata Urutan Peraturan Perundang-Undangan",
                "pertanyaan": (
                    "Bagaimana proses pembentukan Undang-Undang di Indonesia? "
                    "Jelaskan tahapan-tahapannya!"
                ),
                "kata_kunci": [
                    "Prolegnas (Program Legislasi Nasional)",
                    "Tahap perencanaan, penyusunan, pembahasan, pengesahan, pengundangan",
                    "Peran DPR dan Presiden dalam legislasi",
                    "Partisipasi publik dalam pembentukan UU",
                ],
                "panduan": ["Proses pembentukan UU", "Peran lembaga dalam legislasi"],
                "tugas": {
                    "nomor": 1,
                    "deskripsi": "Menganalisis dasar dan sumber sistem hukum Indonesia (Modul 1-3).",
                    "poin": [
                        "Jelaskan mengapa Indonesia disebut memiliki sistem hukum campuran!",
                        "Uraikan hierarki peraturan perundang-undangan Indonesia dan asas-asasnya!",
                        "Jelaskan proses pembentukan undang-undang di Indonesia!",
                    ],
                },
            },
            {
                "topik": "Lembaga Peradilan Indonesia",
                "pertanyaan": (
                    "Apa saja lembaga peradilan yang ada di Indonesia? Jelaskan "
                    "kewenangan masing-masing peradilan!"
                ),
                "kata_kunci": [
                    "Mahkamah Agung (MA) dan peradilan di bawahnya",
                    "Mahkamah Konstitusi (MK) – uji materiil UU",
                    "Peradilan umum, agama, militer, tata usaha negara",
                    "Komisi Yudisial dan pengawasan hakim",
                ],
                "panduan": ["Jenis-jenis lembaga peradilan", "Kewenangan masing-masing"],
                "tugas": None,
            },
            {
                "topik": "Hukum Perdata Indonesia",
                "pertanyaan": (
                    "Apa yang dimaksud dengan hukum perdata? Jelaskan ruang lingkup "
                    "hukum perdata yang berlaku di Indonesia!"
                ),
                "kata_kunci": [
                    "KUHPerdata (BW) warisan Belanda",
                    "Hukum orang, hukum keluarga, hukum benda, hukum perikatan, hukum waris",
                    "Asas kebebasan berkontrak (Pasal 1338 KUHPerdata)",
                    "Asas pacta sunt servanda",
                ],
                "panduan": ["Pengertian dan ruang lingkup hukum perdata", "Asas-asas hukum perdata"],
                "tugas": None,
            },
            {
                "topik": "Hukum Pidana Indonesia",
                "pertanyaan": (
                    "Apa yang membedakan hukum pidana dengan hukum perdata? "
                    "Jelaskan asas-asas utama dalam hukum pidana Indonesia!"
                ),
                "kata_kunci": [
                    "KUHP (Wetboek van Strafrecht) dan KUHAP",
                    "Asas legalitas (Pasal 1 KUHP) – nullum crimen nulla poena sine lege",
                    "Unsur-unsur tindak pidana: perbuatan, sifat melawan hukum, kesalahan",
                    "Perbedaan delik aduan dan delik biasa",
                ],
                "panduan": ["Perbedaan pidana-perdata", "Asas legalitas dan penerapannya"],
                "tugas": {
                    "nomor": 2,
                    "deskripsi": "Menganalisis lembaga peradilan dan hukum substansif (Modul 4-6).",
                    "poin": [
                        "Jelaskan struktur dan kewenangan lembaga peradilan di Indonesia!",
                        "Uraikan ruang lingkup hukum perdata Indonesia beserta asas-asasnya!",
                        "Apa yang dimaksud asas legalitas dalam hukum pidana? Berikan contohnya!",
                    ],
                },
            },
            {
                "topik": "Hukum Dagang Indonesia",
                "pertanyaan": (
                    "Apa hubungan antara hukum dagang dengan hukum perdata? "
                    "Jelaskan prinsip-prinsip dasar hukum dagang di Indonesia!"
                ),
                "kata_kunci": [
                    "KUHD (Kitab UU Hukum Dagang)",
                    "Asas lex specialis: KUHD mengesampingkan KUHPerdata",
                    "Perusahaan, pedagang, dan kegiatan usaha",
                    "PT, CV, Firma, koperasi sebagai bentuk badan usaha",
                ],
                "panduan": ["Hubungan KUHD-KUHPerdata", "Bentuk-bentuk badan usaha"],
                "tugas": None,
            },
            {
                "topik": "Hukum Agraria Indonesia",
                "pertanyaan": (
                    "Bagaimana UUPA mengatur hak-hak atas tanah di Indonesia? "
                    "Jelaskan perbedaan HM, HGU, HGB, dan HP!"
                ),
                "kata_kunci": [
                    "UUPA (UU No. 5 Tahun 1960) – asas nasionalitas",
                    "Hak Milik (HM) – terkuat, terpenuh",
                    "Hak Guna Usaha (HGU), Hak Guna Bangunan (HGB), Hak Pakai (HP)",
                    "Asas domein verklaring dihapus → tanah dikuasai negara",
                ],
                "panduan": ["Asas-asas UUPA", "Perbedaan jenis-jenis hak atas tanah"],
                "tugas": None,
            },
            {
                "topik": "Hukum Internasional dalam Sistem Hukum Indonesia",
                "pertanyaan": (
                    "Bagaimana Indonesia memandang hubungan antara hukum nasional "
                    "dengan hukum internasional? Jelaskan teori monisme dan dualisme!"
                ),
                "kata_kunci": [
                    "Teori monisme (primat HI) vs dualisme (HI dan HN terpisah)",
                    "Indonesia cenderung dualis – ratifikasi melalui UU",
                    "Pacta sunt servanda dalam perjanjian internasional",
                    "Contoh: ratifikasi konvensi HAM internasional",
                ],
                "panduan": ["Teori monisme vs dualisme", "Praktik Indonesia dalam ratifikasi"],
                "tugas": {
                    "nomor": 3,
                    "deskripsi": "Menganalisis hukum khusus dan hukum internasional (Modul 7-9).",
                    "poin": [
                        "Jelaskan prinsip-prinsip dasar hukum dagang Indonesia!",
                        "Uraikan sistem hak atas tanah dalam UUPA dan perbedaan jenis haknya!",
                        "Bagaimana Indonesia menyikapi hubungan hukum nasional dan hukum internasional?",
                    ],
                },
            },
        ],
    },

    # ── 3. Bahasa Indonesia ─────────────────────────────────────────────────
    {
        "nama": "Bahasa Indonesia",
        "kode": "MKWU4108",
        "deskripsi": (
            "Mata kuliah ini membahas kedudukan, fungsi, dan penggunaan bahasa "
            "Indonesia yang baik dan benar dalam konteks akademik dan profesional."
        ),
        "modul": [
            {
                "topik": "Kedudukan dan Fungsi Bahasa Indonesia",
                "pertanyaan": (
                    "Jelaskan kedudukan bahasa Indonesia sebagai bahasa nasional "
                    "dan bahasa negara serta fungsinya masing-masing!"
                ),
                "kata_kunci": [
                    "Bahasa nasional (Sumpah Pemuda 1928): lambang identitas, alat pemersatu",
                    "Bahasa negara (UUD 1945 Pasal 36): bahasa resmi kenegaraan",
                    "Fungsi: komunikasi, ekspresi diri, integrasi nasional",
                    "UU No. 24 Tahun 2009 tentang Bendera, Bahasa, dan Lambang Negara",
                ],
                "panduan": ["Kedudukan sebagai bahasa nasional", "Fungsi sebagai bahasa negara"],
                "tugas": None,
            },
            {
                "topik": "Ejaan Bahasa Indonesia (EYD/PUEBI)",
                "pertanyaan": (
                    "Apa perbedaan EYD dengan PUEBI? Berikan contoh penggunaan "
                    "ejaan yang benar sesuai PUEBI!"
                ),
                "kata_kunci": [
                    "PUEBI (Pedoman Umum Ejaan Bahasa Indonesia) – pengganti EYD",
                    "Penulisan huruf kapital, huruf miring, tanda baca",
                    "Penulisan kata depan (di, ke, dari) – dipisah dari kata benda",
                    "Penulisan imbuhan (awalan, akhiran, sisipan, konfiks)",
                ],
                "panduan": ["Perbedaan EYD dan PUEBI", "Contoh penerapan ejaan yang benar"],
                "tugas": None,
            },
            {
                "topik": "Pembentukan Kata",
                "pertanyaan": (
                    "Jelaskan proses pembentukan kata dalam bahasa Indonesia! "
                    "Berikan contoh afiksasi, reduplikasi, dan pemajemukan!"
                ),
                "kata_kunci": [
                    "Afiksasi: prefiks (me-, di-, ke-), sufiks (-an, -kan, -i), konfiks",
                    "Reduplikasi: pengulangan penuh, sebagian, berubah bunyi",
                    "Pemajemukan: kata majemuk (rumah sakit, meja makan)",
                    "Akronim dan singkatan",
                ],
                "panduan": ["Proses morfologis bahasa Indonesia", "Contoh tiap jenis pembentukan"],
                "tugas": {
                    "nomor": 1,
                    "deskripsi": "Menganalisis dasar penggunaan bahasa Indonesia (Modul 1-3).",
                    "poin": [
                        "Jelaskan perbedaan kedudukan bahasa Indonesia sebagai bahasa nasional dan bahasa negara!",
                        "Berikan 10 contoh kesalahan ejaan umum dan perbaikannya sesuai PUEBI!",
                        "Buat 5 contoh kalimat yang menerapkan proses afiksasi, reduplikasi, dan pemajemukan!",
                    ],
                },
            },
            {
                "topik": "Kalimat Efektif",
                "pertanyaan": (
                    "Apa ciri-ciri kalimat efektif? Perbaiki kalimat-kalimat "
                    "tidak efektif berikut dan jelaskan alasannya!"
                ),
                "kata_kunci": [
                    "Ciri kalimat efektif: kesatuan, kepaduan, keparalelan, ketepatan, kehematan",
                    "Subjek-predikat-objek-keterangan (SPOK)",
                    "Menghindari pleonasme, ambiguitas, kontaminasi",
                    "Kalimat aktif vs pasif dalam konteks akademik",
                ],
                "panduan": ["Ciri-ciri kalimat efektif", "Contoh perbaikan kalimat tidak efektif"],
                "tugas": None,
            },
            {
                "topik": "Paragraf",
                "pertanyaan": (
                    "Jelaskan syarat-syarat paragraf yang baik dan perbedaan "
                    "antara paragraf deduktif, induktif, dan campuran!"
                ),
                "kata_kunci": [
                    "Syarat paragraf: kesatuan (unity), kepaduan (coherence), kelengkapan",
                    "Kalimat topik dan kalimat pengembang",
                    "Paragraf deduktif (umum ke khusus), induktif (khusus ke umum)",
                    "Teknik pengembangan: definisi, contoh, perbandingan, sebab-akibat",
                ],
                "panduan": ["Syarat dan struktur paragraf", "Jenis paragraf berdasarkan posisi kalimat topik"],
                "tugas": None,
            },
            {
                "topik": "Karangan",
                "pertanyaan": (
                    "Apa perbedaan antara karangan narasi, deskripsi, eksposisi, "
                    "argumentasi, dan persuasi? Berikan contoh masing-masing!"
                ),
                "kata_kunci": [
                    "Narasi: menceritakan peristiwa, ada alur waktu",
                    "Deskripsi: menggambarkan objek secara detail",
                    "Eksposisi: memaparkan informasi/data",
                    "Argumentasi: membuktikan pendapat dengan bukti",
                    "Persuasi: memengaruhi pembaca untuk bertindak",
                ],
                "panduan": ["Definisi dan ciri tiap jenis karangan", "Contoh paragraf dari tiap jenis"],
                "tugas": {
                    "nomor": 2,
                    "deskripsi": "Menulis paragraf dan karangan yang baik (Modul 4-6).",
                    "poin": [
                        "Tulis 3 paragraf efektif (deduktif, induktif, campuran) bertema hukum!",
                        "Buat karangan eksposisi (300-400 kata) tentang pentingnya supremasi hukum!",
                        "Identifikasi dan perbaiki 5 kalimat tidak efektif dalam teks yang diberikan!",
                    ],
                },
            },
            {
                "topik": "Surat Resmi",
                "pertanyaan": (
                    "Apa saja komponen surat resmi? Tulislah contoh surat resmi "
                    "permohonan dari mahasiswa ke instansi pemerintah!"
                ),
                "kata_kunci": [
                    "Komponen surat resmi: kop surat, nomor, tanggal, perihal, lampiran",
                    "Bagian isi: pembukaan, isi pokok, penutup",
                    "Bahasa surat: formal, lugas, hormat",
                    "Jenis surat dinas, surat tugas, surat keterangan",
                ],
                "panduan": ["Komponen surat resmi", "Contoh surat resmi yang benar"],
                "tugas": None,
            },
            {
                "topik": "Karya Ilmiah",
                "pertanyaan": (
                    "Jelaskan sistematika penulisan karya ilmiah yang baik! "
                    "Bagaimana cara membuat kutipan dan daftar pustaka yang benar?"
                ),
                "kata_kunci": [
                    "Sistematika: pendahuluan, tinjauan pustaka, metode, pembahasan, kesimpulan",
                    "Kutipan langsung dan tidak langsung",
                    "Penulisan referensi: APA Style, Chicago Style",
                    "Plagiarisme dan cara menghindarinya",
                ],
                "panduan": ["Sistematika karya ilmiah", "Format kutipan dan daftar pustaka"],
                "tugas": None,
            },
            {
                "topik": "Presentasi dan Komunikasi Lisan",
                "pertanyaan": (
                    "Apa saja teknik presentasi yang efektif? Bagaimana cara "
                    "menyampaikan argumen secara lisan dalam diskusi akademik?"
                ),
                "kata_kunci": [
                    "Teknik pembukaan presentasi yang menarik",
                    "Bahasa tubuh (body language) dan kontak mata",
                    "Penggunaan media visual (slide, grafik)",
                    "Teknik tanya-jawab dan merespons sanggahan",
                ],
                "panduan": ["Teknik presentasi efektif", "Cara berargumentasi dalam diskusi"],
                "tugas": {
                    "nomor": 3,
                    "deskripsi": "Mempraktikkan kemampuan menulis surat dan karya ilmiah (Modul 7-9).",
                    "poin": [
                        "Tulislah surat resmi permohonan beasiswa dengan format yang benar!",
                        "Buat abstrak (150-200 kata) dari artikel hukum yang kamu baca!",
                        "Susun daftar pustaka dari 5 sumber yang kamu gunakan (format APA)!",
                    ],
                },
            },
        ],
    },

    # ── 4. Ilmu Negara ──────────────────────────────────────────────────────
    {
        "nama": "Ilmu Negara",
        "kode": "HKUM4207",
        "deskripsi": (
            "Mata kuliah ini membahas teori tentang negara, meliputi asal-usul, unsur, "
            "tujuan, bentuk negara, kedaulatan, konstitusi, dan negara hukum."
        ),
        "modul": [
            {
                "topik": "Pengertian dan Ruang Lingkup Ilmu Negara",
                "pertanyaan": (
                    "Apa yang membedakan ilmu negara dengan hukum tata negara? "
                    "Jelaskan objek kajian ilmu negara!"
                ),
                "kata_kunci": [
                    "Ilmu negara: ilmu abstrak-umum tentang negara",
                    "HTN: ilmu konkret tentang hukum negara tertentu",
                    "Objek kajian: hakikat, asal-usul, tujuan, bentuk negara",
                    "Tokoh: Jellinek (Allgemeine Staatslehre), Kranenburg",
                ],
                "panduan": ["Definisi dan objek ilmu negara", "Perbedaan dengan HTN"],
                "tugas": None,
            },
            {
                "topik": "Asal Usul Negara",
                "pertanyaan": (
                    "Jelaskan teori-teori tentang asal usul negara! "
                    "Teori mana yang paling sesuai menjelaskan terbentuknya NKRI?"
                ),
                "kata_kunci": [
                    "Teori ketuhanan (theokratis) – negara atas kehendak Tuhan",
                    "Teori kekuatan – negara terbentuk dari penaklukan",
                    "Teori perjanjian (kontrak sosial) – Hobbes, Locke, Rousseau",
                    "Teori organis – negara seperti organisme hidup",
                ],
                "panduan": ["Uraian tiap teori asal negara", "Relevansi dengan terbentuknya NKRI"],
                "tugas": None,
            },
            {
                "topik": "Unsur-Unsur Negara",
                "pertanyaan": (
                    "Apa saja unsur-unsur negara menurut Konvensi Montevideo 1933? "
                    "Apakah semua unsur ini terpenuhi oleh Indonesia?"
                ),
                "kata_kunci": [
                    "Konvensi Montevideo: rakyat, wilayah, pemerintah, pengakuan negara lain",
                    "Rakyat: penduduk + warga negara",
                    "Wilayah: darat, laut (ZEE 200 mil), udara (kedaulatan penuh)",
                    "Pemerintah yang berdaulat (de facto dan de jure)",
                ],
                "panduan": ["Empat unsur negara", "Aplikasi pada NKRI"],
                "tugas": {
                    "nomor": 1,
                    "deskripsi": "Menganalisis konsep dasar dan pembentukan negara (Modul 1-3).",
                    "poin": [
                        "Jelaskan perbedaan ilmu negara dengan hukum tata negara!",
                        "Uraikan teori-teori asal usul negara dan relevansinya dengan NKRI!",
                        "Analisis pemenuhan unsur-unsur negara oleh Indonesia!",
                    ],
                },
            },
            {
                "topik": "Tujuan dan Fungsi Negara",
                "pertanyaan": (
                    "Jelaskan tujuan negara Indonesia menurut Pembukaan UUD 1945 "
                    "dan kaitkan dengan teori tujuan negara!"
                ),
                "kata_kunci": [
                    "Tujuan NKRI: melindungi segenap bangsa, memajukan kesejahteraan umum, mencerdaskan",
                    "Teori tujuan negara: kekuasaan (Machiavelli), kemakmuran (welfare state), keamanan",
                    "Fungsi negara: regulasi, pelayanan, pemberdayaan, pembangunan",
                    "Negara kesejahteraan (welfare state) dalam konstitusi Indonesia",
                ],
                "panduan": ["Tujuan NKRI dalam Pembukaan UUD 1945", "Kaitkan dengan teori tujuan negara"],
                "tugas": None,
            },
            {
                "topik": "Bentuk Negara dan Bentuk Pemerintahan",
                "pertanyaan": (
                    "Apa perbedaan bentuk negara kesatuan dengan federasi? "
                    "Mengapa Indonesia memilih bentuk negara kesatuan?"
                ),
                "kata_kunci": [
                    "Negara kesatuan (unitaris) vs federal (serikat)",
                    "Sentralisasi vs desentralisasi dalam negara kesatuan",
                    "Bentuk pemerintahan: monarki, republik, oligarki",
                    "Alasan NKRI memilih negara kesatuan (Pasal 1 ayat 1 UUD 1945)",
                ],
                "panduan": ["Perbedaan kesatuan-federal", "Alasan pilihan bentuk negara Indonesia"],
                "tugas": None,
            },
            {
                "topik": "Teori Kedaulatan",
                "pertanyaan": (
                    "Jelaskan berbagai teori kedaulatan! Teori kedaulatan "
                    "mana yang dianut Indonesia? Berikan bukti dari konstitusi!"
                ),
                "kata_kunci": [
                    "Kedaulatan Tuhan (theokratis), kedaulatan raja (absolutisme)",
                    "Kedaulatan rakyat (demokrasi) – Rousseau, Locke",
                    "Kedaulatan hukum (rechtssoevereiniteit) – Kelsen, Krabbe",
                    "Indonesia: kedaulatan rakyat (Pasal 1 ayat 2 UUD 1945)",
                ],
                "panduan": ["Macam-macam teori kedaulatan", "Bukti teori yang dianut Indonesia"],
                "tugas": {
                    "nomor": 2,
                    "deskripsi": "Menganalisis tujuan, bentuk, dan kedaulatan negara (Modul 4-6).",
                    "poin": [
                        "Kaitkan tujuan NKRI dalam Pembukaan UUD 1945 dengan teori tujuan negara!",
                        "Bandingkan kelebihan dan kekurangan bentuk negara kesatuan dan federal!",
                        "Buktikan teori kedaulatan yang dianut Indonesia dari teks UUD 1945!",
                    ],
                },
            },
            {
                "topik": "Konstitusi dan Konstitusionalisme",
                "pertanyaan": (
                    "Apa fungsi konstitusi dalam negara modern? Jelaskan "
                    "sejarah perubahan (amendemen) UUD 1945!"
                ),
                "kata_kunci": [
                    "Fungsi konstitusi: membatasi kekuasaan, menjamin HAM, mengatur struktur negara",
                    "Konstitusionalisme: kekuasaan dibatasi oleh hukum",
                    "Amendemen UUD 1945 I-IV (1999-2002): perubahan struktur kekuasaan",
                    "Lembaga baru pasca amendemen: MK, DPD, KY",
                ],
                "panduan": ["Fungsi konstitusi", "Sejarah amendemen UUD 1945"],
                "tugas": None,
            },
            {
                "topik": "Lembaga-Lembaga Negara",
                "pertanyaan": (
                    "Jelaskan struktur lembaga negara Indonesia pasca amendemen UUD 1945 "
                    "dan prinsip pemisahan/pembagian kekuasaan!"
                ),
                "kata_kunci": [
                    "Trias Politica: legislatif (MPR/DPR/DPD), eksekutif (Presiden), yudikatif (MA/MK)",
                    "Check and balances antar lembaga",
                    "Lembaga independen: KPU, KPK, Ombudsman, BI",
                    "Hubungan pusat-daerah: desentralisasi dan otonomi daerah",
                ],
                "panduan": ["Struktur lembaga negara", "Prinsip checks and balances"],
                "tugas": None,
            },
            {
                "topik": "Negara Hukum dan Demokrasi",
                "pertanyaan": (
                    "Apa ciri-ciri negara hukum (rechtsstaat)? Bagaimana "
                    "implementasi negara hukum dan demokrasi di Indonesia?"
                ),
                "kata_kunci": [
                    "Rechtsstaat (Stahl): hak dasar, pemisahan kekuasaan, pemerintahan berdasar UU, peradilan TUN",
                    "Rule of Law (Dicey): supremasi hukum, persamaan di hadapan hukum, konstitusi",
                    "Negara hukum Indonesia (Pasal 1 ayat 3 UUD 1945)",
                    "Demokrasi pancasila: musyawarah mufakat, perwakilan rakyat",
                ],
                "panduan": ["Ciri-ciri rechtsstaat dan rule of law", "Implementasi di Indonesia"],
                "tugas": {
                    "nomor": 3,
                    "deskripsi": "Menganalisis konstitusi, lembaga negara, dan negara hukum (Modul 7-9).",
                    "poin": [
                        "Jelaskan perubahan mendasar setelah amendemen UUD 1945!",
                        "Analisis struktur lembaga negara dan prinsip checks and balances di Indonesia!",
                        "Bagaimana Indonesia mewujudkan konsep negara hukum dan demokrasi?",
                    ],
                },
            },
        ],
    },

    # ── 5. Hukum Administrasi Negara ────────────────────────────────────────
    {
        "nama": "Hukum Administrasi Negara",
        "kode": "HKUM4407",
        "deskripsi": (
            "Mata kuliah ini membahas hukum yang mengatur organisasi, perbuatan, "
            "dan pertanggungjawaban pemerintah dalam menjalankan tugas kenegaraan."
        ),
        "modul": [
            {
                "topik": "Pengertian dan Ruang Lingkup HAN",
                "pertanyaan": (
                    "Apa yang dimaksud dengan Hukum Administrasi Negara? "
                    "Jelaskan ruang lingkupnya dan perbedaannya dengan HTN!"
                ),
                "kata_kunci": [
                    "HAN = hukum yang mengatur pemerintah dalam arti sempit",
                    "HTN: mengatur struktur negara; HAN: mengatur pelaksanaan kekuasaan",
                    "Objek HAN: keputusan TUN, izin, sanksi administratif",
                    "Tokoh: van Vollenhoven, Logemann, Philipus M. Hadjon",
                ],
                "panduan": ["Definisi dan ruang lingkup HAN", "Perbedaan HAN dengan HTN"],
                "tugas": None,
            },
            {
                "topik": "Sumber Hukum Administrasi Negara",
                "pertanyaan": (
                    "Sebutkan dan jelaskan sumber-sumber hukum administrasi negara! "
                    "Apa peran asas-asas umum pemerintahan yang baik (AUPB)?"
                ),
                "kata_kunci": [
                    "Sumber tertulis: UU, Peraturan Pemerintah, Peraturan Presiden",
                    "Sumber tidak tertulis: kebiasaan administrasi, yurisprudensi PTUN",
                    "AUPB (UU AP No. 30/2014): asas kepastian hukum, kemanfaatan, ketidakberpihakan",
                    "Asas legalitas dalam HAN: wetmatigheid van bestuur",
                ],
                "panduan": ["Sumber-sumber HAN", "AUPB dan aplikasinya"],
                "tugas": None,
            },
            {
                "topik": "Organisasi Pemerintahan",
                "pertanyaan": (
                    "Jelaskan konsep desentralisasi, dekonsentrasi, dan medebewind "
                    "dalam organisasi pemerintahan Indonesia!"
                ),
                "kata_kunci": [
                    "Desentralisasi: penyerahan wewenang kepada daerah otonom",
                    "Dekonsentrasi: pelimpahan wewenang kepada wakil pemerintah pusat",
                    "Medebewind (tugas pembantuan): menjalankan tugas pusat",
                    "Pemerintah pusat vs daerah (UU No. 23/2014 tentang Pemda)",
                ],
                "panduan": ["Perbedaan desentralisasi-dekonsentrasi-medebewind", "Contoh penerapan di Indonesia"],
                "tugas": {
                    "nomor": 1,
                    "deskripsi": "Menganalisis konsep dasar HAN dan organisasi pemerintahan (Modul 1-3).",
                    "poin": [
                        "Jelaskan perbedaan HAN dengan HTN dan ruang lingkup masing-masing!",
                        "Uraikan asas-asas umum pemerintahan yang baik (AUPB) beserta contohnya!",
                        "Jelaskan perbedaan desentralisasi, dekonsentrasi, dan tugas pembantuan!",
                    ],
                },
            },
            {
                "topik": "Perbuatan Pemerintahan",
                "pertanyaan": (
                    "Apa saja jenis-jenis perbuatan pemerintahan? Apa perbedaan "
                    "antara perbuatan hukum publik dengan perbuatan hukum privat pemerintah?"
                ),
                "kata_kunci": [
                    "Perbuatan hukum publik: beschikking (KTUN), peraturan (regeling), rencana",
                    "Perbuatan hukum privat: perjanjian perdata, jual beli tanah",
                    "Perbuatan nyata (feitelijke handelingen) – tidak menimbulkan akibat hukum langsung",
                    "Organ/badan pemerintah yang berwenang bertindak",
                ],
                "panduan": ["Jenis-jenis perbuatan pemerintahan", "Perbedaan perbuatan hukum publik-privat"],
                "tugas": None,
            },
            {
                "topik": "Keputusan Tata Usaha Negara (KTUN)",
                "pertanyaan": (
                    "Apa yang dimaksud dengan KTUN? Jelaskan syarat-syarat sahnya "
                    "KTUN dan kapan KTUN dapat dinyatakan batal atau tidak sah!"
                ),
                "kata_kunci": [
                    "KTUN (Pasal 1 angka 9 UU PTUN): penetapan tertulis, pejabat TUN, bersifat konkret-individual-final",
                    "Syarat sah: kewenangan, prosedur, substansi (Pasal 52 UU AP)",
                    "Cacat KTUN: batal demi hukum (null and void) vs dapat dibatalkan (vernietigbaar)",
                    "Contoh KTUN: izin usaha, SK pengangkatan PNS",
                ],
                "panduan": ["Definisi dan unsur KTUN", "Syarat sah dan cacat KTUN"],
                "tugas": None,
            },
            {
                "topik": "Izin (Vergunning)",
                "pertanyaan": (
                    "Apa fungsi izin dalam hukum administrasi negara? "
                    "Jelaskan jenis-jenis izin dan prosedur penerbitannya!"
                ),
                "kata_kunci": [
                    "Izin: pernyataan pemerintah bahwa suatu perbuatan diperbolehkan",
                    "Jenis izin: konstitutif (menciptakan hak baru) vs deklaratoir (mengakui hak)",
                    "Prosedur: permohonan, pemeriksaan, keputusan, pengumuman",
                    "Prinsip OSS (One Single Submission) dalam UU Cipta Kerja",
                ],
                "panduan": ["Fungsi dan jenis izin", "Prosedur penerbitan izin"],
                "tugas": {
                    "nomor": 2,
                    "deskripsi": "Menganalisis perbuatan pemerintahan dan KTUN (Modul 4-6).",
                    "poin": [
                        "Jelaskan jenis-jenis perbuatan pemerintahan beserta contohnya!",
                        "Uraikan syarat-syarat sahnya KTUN dan akibat jika syarat tidak terpenuhi!",
                        "Bagaimana sistem perizinan berusaha berubah setelah UU Cipta Kerja?",
                    ],
                },
            },
            {
                "topik": "Penegakan Hukum Administrasi",
                "pertanyaan": (
                    "Apa saja bentuk sanksi administratif yang dapat dijatuhkan pemerintah? "
                    "Bagaimana prosedur penerapannya?"
                ),
                "kata_kunci": [
                    "Sanksi administratif: teguran, denda, pencabutan izin, paksaan pemerintah",
                    "Paksaan nyata (bestuursdwang) dan uang paksa (dwangsom)",
                    "Prinsip proporsionalitas dalam penjatuhan sanksi",
                    "Perlindungan warga dari penyalahgunaan wewenang (detournement de pouvoir)",
                ],
                "panduan": ["Jenis sanksi administratif", "Prosedur dan prinsip penerapannya"],
                "tugas": None,
            },
            {
                "topik": "Peradilan Tata Usaha Negara (PTUN)",
                "pertanyaan": (
                    "Apa kewenangan Peradilan TUN? Siapa yang dapat mengajukan "
                    "gugatan ke PTUN dan apa saja syaratnya?"
                ),
                "kata_kunci": [
                    "PTUN dibentuk UU No. 5/1986 jo UU No. 51/2009",
                    "Kewenangan: menguji keabsahan KTUN",
                    "Penggugat: orang/badan hukum yang kepentingannya dirugikan KTUN",
                    "Tenggang waktu gugatan: 90 hari sejak KTUN diterima",
                ],
                "panduan": ["Kewenangan PTUN", "Syarat dan prosedur gugatan"],
                "tugas": None,
            },
            {
                "topik": "Ombudsman dan Pengawasan Pemerintahan",
                "pertanyaan": (
                    "Apa fungsi Ombudsman RI? Bagaimana sistem pengawasan "
                    "internal dan eksternal pemerintahan di Indonesia?"
                ),
                "kata_kunci": [
                    "Ombudsman RI (UU No. 37/2008): pengawas pelayanan publik",
                    "Maladministrasi: penundaan berlarut, penyimpangan prosedur, nepotisme",
                    "Pengawasan internal: Itjen, BPKP, Inspektorat Daerah",
                    "Pengawasan eksternal: DPR, BPK, Ombudsman, masyarakat/NGO",
                ],
                "panduan": ["Fungsi Ombudsman", "Mekanisme pengawasan internal-eksternal"],
                "tugas": {
                    "nomor": 3,
                    "deskripsi": "Menganalisis penegakan dan pengawasan HAN (Modul 7-9).",
                    "poin": [
                        "Jelaskan jenis sanksi administratif dan prinsip proporsionalitasnya!",
                        "Uraikan kewenangan PTUN dan prosedur mengajukan gugatan!",
                        "Bagaimana peran Ombudsman dan lembaga pengawas lain dalam pemerintahan Indonesia?",
                    ],
                },
            },
        ],
    },

    # ── 6. PKN ───────────────────────────────────────────────────────────────
    {
        "nama": "Pendidikan Kewarganegaraan (PKN)",
        "kode": "MKWU4109",
        "deskripsi": (
            "Mata kuliah ini membahas konsep kewarganegaraan, identitas nasional, "
            "demokrasi, HAM, geopolitik, otonomi daerah, dan ketahanan nasional Indonesia."
        ),
        "modul": [
            {
                "topik": "Identitas Nasional",
                "pertanyaan": (
                    "Apa yang dimaksud dengan identitas nasional? Apa saja "
                    "unsur pembentuk identitas nasional Indonesia?"
                ),
                "kata_kunci": [
                    "Identitas nasional: ciri khas yang membedakan satu bangsa dari bangsa lain",
                    "Unsur: bahasa, budaya, sejarah, wilayah, agama, Pancasila, Bhinneka Tunggal Ika",
                    "Globalisasi sebagai tantangan identitas nasional",
                    "Nasionalisme dan patriotisme dalam konteks modern",
                ],
                "panduan": ["Definisi dan unsur identitas nasional", "Tantangan globalisasi"],
                "tugas": None,
            },
            {
                "topik": "Negara dan Konstitusi",
                "pertanyaan": (
                    "Mengapa konstitusi penting bagi suatu negara? Jelaskan "
                    "fungsi dan kedudukan UUD 1945 dalam sistem hukum Indonesia!"
                ),
                "kata_kunci": [
                    "Konstitusi sebagai hukum tertinggi (grundnorm)",
                    "Fungsi: membatasi kekuasaan, menjamin hak warga, mengatur lembaga negara",
                    "UUD 1945 sebagai konstitusi Indonesia – amendemen 4 kali",
                    "Prinsip supremasi konstitusi",
                ],
                "panduan": ["Fungsi konstitusi", "Kedudukan UUD 1945 dalam sistem hukum"],
                "tugas": None,
            },
            {
                "topik": "Demokrasi Indonesia",
                "pertanyaan": (
                    "Apa yang membedakan demokrasi Pancasila dengan demokrasi "
                    "liberal dan sosialis? Jelaskan perkembangan demokrasi di Indonesia!"
                ),
                "kata_kunci": [
                    "Demokrasi Pancasila: musyawarah mufakat, kekeluargaan, gotong royong",
                    "Demokrasi liberal: kebebasan individu, suara mayoritas",
                    "Demokrasi sosialis: kepentingan kolektif, peran negara besar",
                    "Periode: demokrasi parlementer, Terpimpin, Orde Baru, Reformasi",
                ],
                "panduan": ["Perbedaan model demokrasi", "Perkembangan demokrasi Indonesia"],
                "tugas": {
                    "nomor": 1,
                    "deskripsi": "Menganalisis identitas, konstitusi, dan demokrasi Indonesia (Modul 1-3).",
                    "poin": [
                        "Apa saja unsur identitas nasional Indonesia dan mengapa penting dipertahankan?",
                        "Jelaskan fungsi UUD 1945 sebagai konstitusi Indonesia!",
                        "Bandingkan demokrasi Pancasila dengan demokrasi liberal!",
                    ],
                },
            },
            {
                "topik": "Hak dan Kewajiban Warga Negara",
                "pertanyaan": (
                    "Apa saja hak dan kewajiban warga negara Indonesia menurut "
                    "UUD 1945? Bagaimana HAM dijamin dalam konstitusi?"
                ),
                "kata_kunci": [
                    "Hak: pendidikan, pekerjaan, beragama, berpendapat (Pasal 27-34 UUD 1945)",
                    "Kewajiban: bela negara, bayar pajak, hormat konstitusi",
                    "HAM dalam Pasal 28A-28J UUD 1945 (amendemen)",
                    "UU No. 39/1999 tentang HAM",
                ],
                "panduan": ["Hak dan kewajiban warga negara", "Jaminan HAM dalam UUD 1945"],
                "tugas": None,
            },
            {
                "topik": "Geopolitik Indonesia",
                "pertanyaan": (
                    "Apa yang dimaksud dengan geopolitik? Jelaskan Wawasan Nusantara "
                    "sebagai geopolitik Indonesia!"
                ),
                "kata_kunci": [
                    "Geopolitik: pengaruh faktor geografis pada kebijakan negara",
                    "Wawasan Nusantara: kesatuan wilayah, bangsa, budaya, dan pertahanan",
                    "UNCLOS 1982: ZEE, landas kontinen, laut teritorial",
                    "Archipelagic state (negara kepulauan) – konsep yang diperjuangkan Indonesia",
                ],
                "panduan": ["Definisi geopolitik", "Wawasan Nusantara dan implementasinya"],
                "tugas": None,
            },
            {
                "topik": "Otonomi Daerah",
                "pertanyaan": (
                    "Apa tujuan otonomi daerah? Bagaimana pembagian kewenangan antara "
                    "pusat dan daerah dalam sistem otonomi Indonesia saat ini?"
                ),
                "kata_kunci": [
                    "Otonomi daerah: UU No. 23/2014 tentang Pemerintahan Daerah",
                    "Urusan wajib (layanan dasar & non dasar) dan urusan pilihan",
                    "Urusan pemerintahan absolut: HanKam, moneter, yustisi, agama, politik luar negeri",
                    "DAU, DAK, Dana Bagi Hasil sebagai sumber pendapatan daerah",
                ],
                "panduan": ["Tujuan otonomi daerah", "Pembagian urusan pusat-daerah"],
                "tugas": {
                    "nomor": 2,
                    "deskripsi": "Menganalisis HAM, geopolitik, dan otonomi daerah (Modul 4-6).",
                    "poin": [
                        "Uraikan hak dan kewajiban warga negara Indonesia yang dijamin UUD 1945!",
                        "Jelaskan konsep Wawasan Nusantara dalam konteks geopolitik Indonesia!",
                        "Bagaimana pembagian kewenangan pemerintah pusat dan daerah di Indonesia?",
                    ],
                },
            },
            {
                "topik": "Ketahanan Nasional",
                "pertanyaan": (
                    "Apa yang dimaksud dengan ketahanan nasional? Jelaskan konsep "
                    "Astagatra dalam ketahanan nasional Indonesia!"
                ),
                "kata_kunci": [
                    "Ketahanan nasional: kemampuan bangsa menghadapi ancaman, hambatan, gangguan",
                    "Astagatra: Trigatra (geografi, SDA, demografi) + Pancagatra (ideologi, politik, ekonomi, sosbudaya, HanKam)",
                    "Ancaman: militer, non-militer (terorisme, narkoba, hoaks)",
                    "Bela negara dalam perspektif modern (non-militer)",
                ],
                "panduan": ["Definisi ketahanan nasional", "Astagatra dan komponen ketahanan"],
                "tugas": None,
            },
            {
                "topik": "Masyarakat Madani",
                "pertanyaan": (
                    "Apa yang dimaksud dengan masyarakat madani (civil society)? "
                    "Apa perannya dalam demokrasi Indonesia?"
                ),
                "kata_kunci": [
                    "Masyarakat madani: masyarakat yang mandiri, demokratis, menjunjung hukum",
                    "Ciri: pluralisme, toleransi, kebebasan berorganisasi, rule of law",
                    "Peran NGO, ormas, media dalam demokrasi",
                    "Tantangan: polarisasi, hoaks, intoleransi",
                ],
                "panduan": ["Konsep masyarakat madani", "Perannya dalam demokrasi Indonesia"],
                "tugas": None,
            },
            {
                "topik": "Integrasi Nasional",
                "pertanyaan": (
                    "Apa faktor pendorong dan penghambat integrasi nasional di Indonesia? "
                    "Bagaimana Pancasila berperan dalam menjaga persatuan?"
                ),
                "kata_kunci": [
                    "Faktor pendorong: Pancasila, bahasa Indonesia, sejarah perjuangan bersama",
                    "Faktor penghambat: separatisme, primordialisme, SARA, ketimpangan ekonomi",
                    "Bhinneka Tunggal Ika sebagai semboyan persatuan dalam keberagaman",
                    "Contoh konflik dan solusi integrasi nasional",
                ],
                "panduan": ["Faktor pendorong-penghambat integrasi", "Peran Pancasila sebagai pemersatu"],
                "tugas": {
                    "nomor": 3,
                    "deskripsi": "Menganalisis ketahanan nasional dan integrasi nasional (Modul 7-9).",
                    "poin": [
                        "Jelaskan konsep Astagatra dalam ketahanan nasional Indonesia!",
                        "Apa peran masyarakat madani dalam memperkuat demokrasi?",
                        "Analisis faktor yang mengancam integrasi nasional dan solusinya!",
                    ],
                },
            },
        ],
    },

    # ── 7. Agama Islam ──────────────────────────────────────────────────────
    {
        "nama": "Pendidikan Agama Islam",
        "kode": "MKWU4101",
        "deskripsi": (
            "Mata kuliah ini membahas dasar-dasar ajaran Islam meliputi akidah, "
            "ibadah, akhlak, muamalah, dan hubungan Islam dengan ilmu pengetahuan."
        ),
        "modul": [
            {
                "topik": "Konsep Ketuhanan dalam Islam",
                "pertanyaan": (
                    "Jelaskan konsep tauhid dalam Islam! Apa perbedaan antara "
                    "tauhid rububiyyah, uluhiyyah, dan asma wa sifat?"
                ),
                "kata_kunci": [
                    "Tauhid: keyakinan bahwa Allah SWT adalah satu-satunya Tuhan",
                    "Tauhid Rububiyyah: Allah sebagai pencipta dan pemelihara",
                    "Tauhid Uluhiyyah: hanya Allah yang berhak disembah",
                    "Tauhid Asma wa Sifat: nama dan sifat Allah sesuai Al-Quran",
                ],
                "panduan": ["Konsep tauhid dalam Islam", "Tiga dimensi tauhid"],
                "tugas": None,
            },
            {
                "topik": "Keimanan dan Ketaqwaan",
                "pertanyaan": (
                    "Jelaskan 6 rukun iman dan bagaimana keimanan dapat "
                    "meningkatkan kualitas hidup seorang Muslim!"
                ),
                "kata_kunci": [
                    "6 Rukun Iman: Allah, Malaikat, Kitab, Rasul, Hari Akhir, Qada-Qadar",
                    "Iman = tashdiq bil qalb, iqrar bil lisan, amal bil arkan",
                    "Taqwa: menjalankan perintah dan menjauhi larangan Allah",
                    "Hubungan iman dan amal saleh",
                ],
                "panduan": ["Rukun iman dan penjelasannya", "Kaitan iman dengan taqwa"],
                "tugas": None,
            },
            {
                "topik": "Al-Quran sebagai Sumber Hukum Islam",
                "pertanyaan": (
                    "Jelaskan kedudukan Al-Quran dalam Islam! Bagaimana cara "
                    "Al-Quran menetapkan hukum (ahkam)?"
                ),
                "kata_kunci": [
                    "Al-Quran: kalam Allah, mukjizat terbesar Nabi Muhammad SAW",
                    "Fungsi Al-Quran: petunjuk, pembeda (furqan), obat (syifa)",
                    "Hukum dalam Al-Quran: wajib, sunnah, mubah, makruh, haram",
                    "Metode penetapan hukum: nash qath'i dan nash zhanni",
                ],
                "panduan": ["Kedudukan Al-Quran", "Cara Al-Quran menetapkan hukum"],
                "tugas": {
                    "nomor": 1,
                    "deskripsi": "Menganalisis dasar-dasar akidah Islam (Modul 1-3).",
                    "poin": [
                        "Jelaskan tiga dimensi tauhid dan contoh penerapannya dalam kehidupan!",
                        "Uraikan 6 rukun iman dan dampaknya terhadap perilaku seorang Muslim!",
                        "Bagaimana Al-Quran berperan sebagai sumber hukum Islam?",
                    ],
                },
            },
            {
                "topik": "Sunnah dan Hadits",
                "pertanyaan": (
                    "Apa yang dimaksud dengan sunnah Nabi? Bagaimana ulama "
                    "mengklasifikasikan hadits berdasarkan kualitas sanadnya?"
                ),
                "kata_kunci": [
                    "Sunnah: perkataan (qawliyah), perbuatan (fi'liyah), ketetapan (taqririyah) Nabi",
                    "Hadits shahih, hasan, dhaif, maudhu (palsu)",
                    "Isnad/sanad: rantai perawi hadits",
                    "Ilmu hadits: musthalah al-hadits, jarh wa ta'dil",
                ],
                "panduan": ["Definisi sunnah dan hadits", "Klasifikasi kualitas hadits"],
                "tugas": None,
            },
            {
                "topik": "Hukum Islam (Syariat)",
                "pertanyaan": (
                    "Apa yang dimaksud dengan syariat Islam? Jelaskan tujuan "
                    "syariat (maqashid al-syariah) menurut Imam al-Ghazali!"
                ),
                "kata_kunci": [
                    "Syariat: aturan Allah yang mengatur hubungan manusia-Tuhan dan manusia-manusia",
                    "Maqashid al-syariah: hifdz al-din, nafs, aql, nasl, mal (5 penjagaan)",
                    "Fiqh: pemahaman manusia atas syariat (bisa berbeda antar mazhab)",
                    "Empat mazhab: Hanafi, Maliki, Syafi'i, Hanbali",
                ],
                "panduan": ["Definisi syariat", "Maqashid al-syariah dan aplikasinya"],
                "tugas": None,
            },
            {
                "topik": "Ibadah dalam Islam",
                "pertanyaan": (
                    "Jelaskan 5 rukun Islam dan hikmah di balik masing-masing "
                    "ibadah tersebut dalam kehidupan seorang Muslim!"
                ),
                "kata_kunci": [
                    "5 Rukun Islam: syahadat, shalat, zakat, puasa, haji",
                    "Ibadah mahdhah (khusus) vs ghair mahdhah (umum)",
                    "Hikmah shalat: kedisiplinan, koneksi dengan Allah",
                    "Hikmah zakat: solidaritas sosial, pemerataan ekonomi",
                ],
                "panduan": ["Rukun Islam dan penjelasannya", "Hikmah tiap ibadah"],
                "tugas": {
                    "nomor": 2,
                    "deskripsi": "Menganalisis sumber hukum Islam dan ibadah (Modul 4-6).",
                    "poin": [
                        "Jelaskan perbedaan sunnah qawliyah, fi'liyah, dan taqririyah beserta contohnya!",
                        "Apa yang dimaksud maqashid al-syariah? Berikan contoh penerapannya!",
                        "Jelaskan hikmah ibadah puasa dan zakat dalam perspektif sosial!",
                    ],
                },
            },
            {
                "topik": "Muamalah (Interaksi Sosial dalam Islam)",
                "pertanyaan": (
                    "Apa prinsip-prinsip muamalah dalam Islam? Bagaimana Islam "
                    "mengatur transaksi ekonomi yang halal?"
                ),
                "kata_kunci": [
                    "Muamalah: interaksi sosial, ekonomi, hukum dalam Islam",
                    "Prinsip: halal, tidak riba, tidak gharar (ketidakpastian), tidak maisir (judi)",
                    "Jual beli (bay'), sewa (ijarah), bagi hasil (mudharabah, musyarakah)",
                    "Perbankan syariah: fatwa DSN-MUI",
                ],
                "panduan": ["Prinsip muamalah Islam", "Transaksi ekonomi yang halal"],
                "tugas": None,
            },
            {
                "topik": "Akhlak dan Etika Islam",
                "pertanyaan": (
                    "Apa yang dimaksud dengan akhlak dalam Islam? Bagaimana "
                    "akhlak mulia dapat diterapkan dalam kehidupan profesional?"
                ),
                "kata_kunci": [
                    "Akhlak: sifat batin yang mendorong perbuatan tanpa pikiran panjang",
                    "Akhlak mahmudah (terpuji): jujur, amanah, sabar, rendah hati",
                    "Akhlak mazmumah (tercela): sombong, hasad, ghibah, riya",
                    "Teladan Nabi: shiddiq, amanah, tabligh, fathonah",
                ],
                "panduan": ["Definisi dan jenis akhlak", "Penerapan akhlak mulia di kehidupan profesi"],
                "tugas": None,
            },
            {
                "topik": "Islam dan Ilmu Pengetahuan",
                "pertanyaan": (
                    "Bagaimana pandangan Islam terhadap ilmu pengetahuan? "
                    "Apa kontribusi peradaban Islam dalam pengembangan ilmu?"
                ),
                "kata_kunci": [
                    "Islam mendorong mencari ilmu (QS Al-Alaq: 1-5, hadits thalabul ilm)",
                    "Tidak ada dikotomi ilmu agama vs ilmu umum",
                    "Masa kejayaan Islam: Al-Khawarizmi (aljabar), Ibn Sina (kedokteran), Al-Biruni",
                    "Integrasi ilmu dan iman dalam paradigma Islam",
                ],
                "panduan": ["Pandangan Islam tentang ilmu", "Kontribusi peradaban Islam"],
                "tugas": {
                    "nomor": 3,
                    "deskripsi": "Menganalisis muamalah, akhlak, dan Islam dalam konteks modern (Modul 7-9).",
                    "poin": [
                        "Jelaskan prinsip-prinsip muamalah Islam dan larangan riba beserta alasannya!",
                        "Bagaimana akhlak mulia berperan dalam kehidupan profesional seorang sarjana hukum?",
                        "Uraikan kontribusi peradaban Islam dalam pengembangan ilmu pengetahuan!",
                    ],
                },
            },
        ],
    },

    # ── 8. Pancasila ────────────────────────────────────────────────────────
    {
        "nama": "Pancasila",
        "kode": "MKWU4110",
        "deskripsi": (
            "Mata kuliah ini membahas Pancasila sebagai dasar negara, ideologi, "
            "sistem filsafat, sistem etika, dan nilai pengembangan ilmu pengetahuan."
        ),
        "modul": [
            {
                "topik": "Pancasila dalam Kajian Sejarah Bangsa",
                "pertanyaan": (
                    "Jelaskan proses perumusan Pancasila! Siapa saja tokoh yang "
                    "berperan dalam sidang BPUPKI dan PPKI?"
                ),
                "kata_kunci": [
                    "BPUPKI (29 Mei – 1 Juni 1945): pidato Soekarno, Soepomo, Moh. Yamin",
                    "Piagam Jakarta (22 Juni 1945): versi awal Pancasila dengan 7 kata",
                    "PPKI (18 Agustus 1945): pengesahan Pancasila dan UUD 1945",
                    "Perubahan sila pertama: dihapusnya '...dengan kewajiban menjalankan syariat Islam'",
                ],
                "panduan": ["Kronologi perumusan Pancasila", "Peran tokoh-tokoh perumus"],
                "tugas": None,
            },
            {
                "topik": "Pancasila sebagai Dasar Negara",
                "pertanyaan": (
                    "Apa yang dimaksud Pancasila sebagai dasar negara? Bagaimana "
                    "Pancasila menjadi sumber dari segala sumber hukum?"
                ),
                "kata_kunci": [
                    "Pancasila sebagai grundnorm (norma dasar) bangsa Indonesia",
                    "Pancasila = sumber dari segala sumber hukum (UU No. 12/2011 Pasal 2)",
                    "Setiap peraturan tidak boleh bertentangan dengan Pancasila",
                    "Pancasila sebagai staatsfundamentalnorm – Kelsen",
                ],
                "panduan": ["Kedudukan Pancasila sebagai dasar negara", "Implikasinya pada sistem hukum"],
                "tugas": None,
            },
            {
                "topik": "Pancasila sebagai Ideologi Negara",
                "pertanyaan": (
                    "Apa yang membedakan Pancasila dengan ideologi komunisme "
                    "dan liberalisme? Mengapa Pancasila disebut ideologi terbuka?"
                ),
                "kata_kunci": [
                    "Ideologi: sistem nilai dan kepercayaan yang menjadi pandangan hidup",
                    "Liberalisme: individualisme, pasar bebas, minimal negara",
                    "Komunisme: kepemilikan kolektif, tidak ada kelas, negara dominan",
                    "Pancasila sebagai ideologi terbuka: dinamis, dapat berkembang sesuai zaman",
                ],
                "panduan": ["Perbedaan Pancasila vs ideologi lain", "Konsep ideologi terbuka"],
                "tugas": {
                    "nomor": 1,
                    "deskripsi": "Menganalisis sejarah dan kedudukan Pancasila (Modul 1-3).",
                    "poin": [
                        "Uraikan proses perumusan Pancasila dalam sidang BPUPKI dan PPKI!",
                        "Jelaskan kedudukan Pancasila sebagai sumber dari segala sumber hukum!",
                        "Bandingkan Pancasila sebagai ideologi dengan liberalisme dan komunisme!",
                    ],
                },
            },
            {
                "topik": "Pancasila sebagai Sistem Filsafat",
                "pertanyaan": (
                    "Jelaskan Pancasila sebagai sistem filsafat! Apa yang dimaksud "
                    "dengan sila-sila Pancasila sebagai satu kesatuan yang bulat?"
                ),
                "kata_kunci": [
                    "Filsafat Pancasila: ontologi (hakikat ada), epistemologi (sumber pengetahuan), aksiologi (nilai)",
                    "Kesatuan organis: sila 1 menjiwai sila 2-5, sila 2 dijiwai sila 1",
                    "Pancasila bukan filsafat Barat maupun Timur – asli Indonesia",
                    "Notonagoro: nilai material, vital, kerohanian dalam Pancasila",
                ],
                "panduan": ["Pancasila dalam kajian filsafat", "Kesatuan organis antar sila"],
                "tugas": None,
            },
            {
                "topik": "Pancasila sebagai Sistem Etika",
                "pertanyaan": (
                    "Bagaimana nilai-nilai Pancasila menjadi standar etika dalam "
                    "kehidupan bernegara? Berikan contoh pelanggaran etika Pancasila!"
                ),
                "kata_kunci": [
                    "Etika Pancasila: pedoman perilaku berdasarkan nilai-nilai sila",
                    "Sila 1: etika beragama – toleransi, menghormati perbedaan",
                    "Sila 2: etika kemanusiaan – menghormati HAM",
                    "Sila 3-5: etika persatuan, demokrasi, keadilan sosial",
                    "Contoh pelanggaran: korupsi, diskriminasi, intoleransi",
                ],
                "panduan": ["Pancasila sebagai etika bernegara", "Contoh penerapan dan pelanggaran"],
                "tugas": None,
            },
            {
                "topik": "Pancasila sebagai Dasar Nilai Pengembangan Ilmu",
                "pertanyaan": (
                    "Bagaimana Pancasila menjadi pedoman dalam pengembangan ilmu "
                    "pengetahuan di Indonesia? Apa batasannya?"
                ),
                "kata_kunci": [
                    "Ilmu pengetahuan tidak bebas nilai (value-laden) dalam perspektif Pancasila",
                    "Teknologi harus digunakan untuk kesejahteraan manusia dan keadilan",
                    "Kritik terhadap saintisme (ilmu sebagai satu-satunya kebenaran)",
                    "Contoh: riset harus mempertimbangkan aspek kemanusiaan (etika biomedis)",
                ],
                "panduan": ["Pancasila sebagai landasan nilai iptek", "Batasan etis pengembangan ilmu"],
                "tugas": {
                    "nomor": 2,
                    "deskripsi": "Menganalisis Pancasila sebagai sistem filsafat dan etika (Modul 4-6).",
                    "poin": [
                        "Jelaskan Pancasila sebagai sistem filsafat dan kesatuan organis antar silanya!",
                        "Bagaimana nilai-nilai Pancasila menjadi panduan etika bernegara? Berikan contoh konkret!",
                        "Bagaimana Pancasila membatasi pengembangan ilmu agar tetap manusiawi?",
                    ],
                },
            },
            {
                "topik": "Hubungan Pancasila dengan UUD 1945",
                "pertanyaan": (
                    "Bagaimana hubungan antara Pancasila dengan UUD 1945? "
                    "Di mana Pancasila tercantum dalam UUD 1945?"
                ),
                "kata_kunci": [
                    "Pancasila ada dalam Pembukaan UUD 1945 alinea ke-4",
                    "Pembukaan UUD 1945 tidak dapat diubah (mengubah = membubarkan NKRI)",
                    "Hubungan kausal: Pancasila melahirkan UUD 1945",
                    "Pasal-pasal UUD 1945 merupakan penjabaran nilai Pancasila",
                ],
                "panduan": ["Letak Pancasila dalam UUD 1945", "Hubungan kausal Pancasila-UUD"],
                "tugas": None,
            },
            {
                "topik": "Implementasi Pancasila dalam Berbagai Bidang",
                "pertanyaan": (
                    "Bagaimana nilai-nilai Pancasila diimplementasikan dalam bidang "
                    "hukum, ekonomi, dan sosial budaya di Indonesia?"
                ),
                "kata_kunci": [
                    "Bidang hukum: supremasi hukum, persamaan di depan hukum (sila 2, 5)",
                    "Bidang ekonomi: Pasal 33 UUD 1945 – ekonomi kerakyatan (sila 5)",
                    "Bidang sosial budaya: toleransi, gotong royong (sila 3, 2)",
                    "Tantangan implementasi: korupsi, ketimpangan, radikalisme",
                ],
                "panduan": ["Implementasi Pancasila per bidang kehidupan", "Hambatan dan solusi"],
                "tugas": None,
            },
            {
                "topik": "Tantangan Pancasila di Era Globalisasi",
                "pertanyaan": (
                    "Apa saja tantangan yang dihadapi Pancasila di era globalisasi? "
                    "Bagaimana generasi muda dapat memperkuat nilai Pancasila?"
                ),
                "kata_kunci": [
                    "Tantangan: liberalisme, sekularisme, radikalisme, hoaks, disinformasi",
                    "Lunturnya nilai gotong royong dan kebersamaan",
                    "Peran pendidikan Pancasila di sekolah dan kampus",
                    "Penguatan Pancasila melalui media sosial, seni budaya, komunitas",
                ],
                "panduan": ["Tantangan Pancasila era globalisasi", "Peran generasi muda"],
                "tugas": {
                    "nomor": 3,
                    "deskripsi": "Menganalisis implementasi dan masa depan Pancasila (Modul 7-9).",
                    "poin": [
                        "Analisis implementasi Pancasila dalam bidang hukum dan ekonomi Indonesia!",
                        "Jelaskan hubungan kausal Pancasila dengan UUD 1945!",
                        "Bagaimana cara memperkuat nilai Pancasila menghadapi tantangan globalisasi?",
                    ],
                },
            },
        ],
    },
]


# ═══════════════════════════════════════════════════════════════════════════════
# FUNGSI UTAMA GENERATE PDF
# ═══════════════════════════════════════════════════════════════════════════════

def generate_pdf(matkul_data, styles, nomor):
    nama  = matkul_data["nama"]
    kode  = matkul_data["kode"]
    fname = f"{nomor:02d}_{kode}_{nama.replace(' ', '_').replace('/', '-')}.pdf"
    path  = os.path.join(OUTPUT_DIR, fname)

    doc = SimpleDocTemplate(
        path, pagesize=A4,
        leftMargin=2*cm, rightMargin=2*cm,
        topMargin=2*cm, bottomMargin=2*cm,
        title=f"Template {nama}",
        author="UT S1 Hukum – Template Generator",
    )

    story = []

    # Cover
    story += halaman_cover(nama, kode, matkul_data["deskripsi"], styles)

    # Modul per modul
    for i, modul in enumerate(matkul_data["modul"], 1):
        block = []
        block.append(header_modul(i, modul["topik"], styles))
        block.append(Spacer(1, 0.3*cm))

        # Diskusi
        block += blok_template_diskusi(
            i,
            modul["pertanyaan"],
            modul["kata_kunci"],
            modul["panduan"],
            styles
        )

        # Tugas (jika ada di modul ini)
        if modul.get("tugas"):
            t = modul["tugas"]
            block += blok_tugas(t["nomor"], t["deskripsi"], t["poin"], styles)

        block.append(HRFlowable(width="100%", thickness=1,
                                color=ABU_BORDER, spaceAfter=8))

        # Hindari pemecahan di tengah modul kalau muat
        story.append(KeepTogether(block[:6]))
        story += block[6:]

        if i < len(matkul_data["modul"]):
            story.append(PageBreak())

    doc.build(story)
    print(f"  [OK] {fname}")
    return path


def main():
    styles = buat_styles()
    print("Membuat PDF template untuk 8 matkul UT S1 Hukum...")
    paths = []
    for i, mk in enumerate(MATKUL, 1):
        paths.append(generate_pdf(mk, styles, i))
    print(f"\nSelesai! {len(paths)} PDF dibuat di folder: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
