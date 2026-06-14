#!/usr/bin/env python3
"""Generate Diskusi 8 - semua 8 matkul UT S1 Hukum"""

from docx import Document
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

OUTPUT = "/home/user/Master-Claude-for-Legal/tools/soal_output/Diskusi8_S1Hukum_UT.docx"

# ─── Jawaban per matkul ───────────────────────────────────────────────────────

DISKUSI = [

# ══════════════════════════════════════════════════════════════════════════════
{
"matkul": "Bahasa Indonesia (MKWU4108) — Diskusi 8",
"isi": """
Assalamualaikum Wr. Wb. / Salam sejahtera untuk kita semua,

Berikut saya paparkan rancangan artikel ilmiah berbasis riset yang saya susun berdasarkan pengamatan terhadap fenomena di lingkungan sekitar.

──────────────────────────────────────
1. JUDUL ARTIKEL (Maksimal 20 Kata)
──────────────────────────────────────
"Pengaruh Penggunaan Media Sosial terhadap Kesadaran Hukum Masyarakat Urban Indonesia di Era Digital"
(16 kata)

──────────────────────────────────────
2. RUMUSAN PERTANYAAN PENELITIAN
──────────────────────────────────────
a. Seberapa besar pengaruh konsumsi konten hukum di media sosial (Instagram, TikTok, YouTube) terhadap tingkat kesadaran hukum masyarakat urban?
b. Faktor-faktor apa yang memengaruhi efektivitas penyebaran informasi hukum melalui media sosial?
c. Platform media sosial manakah yang paling efektif sebagai medium penyuluhan hukum informal?

──────────────────────────────────────
3. TEORI / KONSEP YANG MENDASARI
──────────────────────────────────────
a. Teori Kesadaran Hukum (Lawrence M. Friedman, 1975): hukum berfungsi optimal apabila masyarakat mengetahui (legal knowledge), memahami (legal understanding), menyikapi (legal attitude), dan mematuhi (legal behavior) norma hukum yang berlaku.
b. Teori Difusi Inovasi (Everett M. Rogers, 2003): informasi hukum menyebar melalui saluran komunikasi modern—termasuk media sosial—kepada khalayak yang lebih luas dan beragam.
c. Teori Uses & Gratifications (Katz, Blumler & Gurevitch, 1974): individu secara aktif memilih media berdasarkan kebutuhan kognitif, afektif, dan integrasi sosialnya.

──────────────────────────────────────
4. RANCANGAN HASIL PENELITIAN (Maks. 200 Kata)
──────────────────────────────────────
Penelitian ini menggunakan pendekatan mixed methods. Secara kuantitatif, survei daring kepada 150 responden masyarakat urban berusia 18–40 tahun mengukur tingkat kesadaran hukum sebelum dan sesudah konsumsi konten hukum di media sosial selama 30 hari. Secara kualitatif, wawancara mendalam dilakukan terhadap 10 informan serta tiga kreator konten hukum dengan pengikut di atas 50.000.

Hasil yang diproyeksikan meliputi: (1) pemetaan pola konsumsi konten hukum masyarakat urban berdasarkan platform dan durasi; (2) derajat pengaruh media sosial terhadap pemahaman hak dan kewajiban hukum; (3) identifikasi faktor pendorong dan penghambat penyerapan informasi hukum secara daring; serta (4) rekomendasi bagi pemerintah dan lembaga bantuan hukum dalam mengoptimalkan media sosial sebagai kanal penyuluhan.

Data kuantitatif dianalisis menggunakan uji regresi linear sederhana, sedangkan data kualitatif dianalisis secara tematik. Penelitian ini diharapkan memberikan kontribusi akademis berupa model strategi penyuluhan hukum berbasis digital yang lebih inklusif, efisien, dan menjangkau kelompok masyarakat yang selama ini sulit terlayani metode konvensional.

──────────────────────────────────────
REFERENSI
──────────────────────────────────────
• Friedman, L. M. (1975). The Legal System: A Social Science Perspective. Russell Sage Foundation.
• Rogers, E. M. (2003). Diffusion of Innovations (5th ed.). Free Press.
• Katz, E., Blumler, J. G., & Gurevitch, M. (1974). Utilization of mass communication by the individual. The Uses of Mass Communications, 19–32.

Demikian rancangan artikel ilmiah saya. Mohon masukan dan saran dari Tutor serta rekan mahasiswa. Terima kasih.
""".strip()
},

# ══════════════════════════════════════════════════════════════════════════════
{
"matkul": "Hukum Administrasi Negara (HKUM4407) — Diskusi 8",
"isi": """
Assalamualaikum Wr. Wb. / Salam sejahtera,

Berikut analisis saya terhadap Program "Pulih–Mandiri–Aman" yang dijalankan Dinas Sosial kabupaten dalam konteks Hukum Administrasi Negara.

──────────────────────────────────────
1. HUKUM KESEJAHTERAAN SOSIAL & UNSUR-UNSURNYA
──────────────────────────────────────
Berdasarkan Pasal 1 angka 1 UU No. 11 Tahun 2009 tentang Kesejahteraan Sosial, penyelenggaraan kesejahteraan sosial adalah upaya yang terarah, terpadu, dan berkelanjutan yang dilakukan pemerintah, pemerintah daerah, dan masyarakat dalam bentuk pelayanan sosial guna memenuhi kebutuhan dasar setiap warga negara.

Unsur-unsurnya meliputi:
• Subjek: Penyandang Masalah Kesejahteraan Sosial (PMKS) — keluarga miskin, lansia terlantar, disabilitas.
• Penyelenggara: pemerintah pusat, pemerintah daerah, masyarakat, dan dunia usaha.
• Bentuk layanan: rehabilitasi sosial, jaminan sosial, pemberdayaan sosial, dan perlindungan sosial.
• Tujuan: terpenuhinya kebutuhan material, spiritual, dan sosial agar warga dapat hidup layak dan mandiri.

──────────────────────────────────────
2. MAKNA REHABILITASI, JAMINAN, & PEMBERDAYAAN SOSIAL
──────────────────────────────────────
• Rehabilitasi Sosial (Pasal 7 UU 11/2009): upaya memulihkan dan mengembangkan kemampuan seseorang yang mengalami disfungsi sosial agar dapat melaksanakan fungsi sosialnya secara wajar (konseling, pengasuhan, bimbingan).
• Jaminan Sosial (UU No. 40 Tahun 2004 tentang SJSN): mekanisme perlindungan dari risiko sosial-ekonomi (sakit, kemiskinan, kematian) melalui iuran wajib maupun bantuan iuran dari negara (PBI-JKN).
• Pemberdayaan Sosial (Pasal 12 UU 11/2009): upaya menguatkan kapasitas individu/komunitas agar mandiri secara ekonomi dan sosial, antara lain melalui pelatihan keterampilan dan akses modal usaha.

──────────────────────────────────────
3. KLASIFIKASI KOMPONEN PROGRAM "PULIH–MANDIRI–AMAN"
──────────────────────────────────────
No | Komponen Program                                          | Klasifikasi          | Alasan
1  | Layanan konseling, pengasuhan sementara, rujukan panti    | Rehabilitasi Sosial  | Bertujuan memulihkan fungsi sosial klien yang mengalami disfungsi (Pasal 7 UU 11/2009)
2  | Pendaftaran jaminan kesehatan (PBI-JKN)                   | Jaminan Sosial       | Memberikan perlindungan risiko kesehatan melalui skema BPJS berbasis iuran negara (UU 40/2004 & UU 24/2011)
3  | Pelatihan keterampilan + bantuan modal usaha kecil        | Pemberdayaan Sosial  | Meningkatkan kapasitas ekonomi agar mandiri (Pasal 12 UU 11/2009)
4  | Bantuan darurat kebakaran + pendampingan akses hukum      | Perlindungan Sosial  | Memberikan perlindungan dari kerentanan dan akses keadilan bagi yang haknya dilanggar (Pasal 14 UU 11/2009)
5  | Peningkatan akses kerja, kesehatan, pendidikan, perumahan | Pemberdayaan Sosial  | Memperluas akses kelompok miskin terhadap sumber daya dan layanan dasar (Pasal 12-13 UU 11/2009)

──────────────────────────────────────
4. PENYELENGGARAAN PENANGGULANGAN KEMISKINAN
──────────────────────────────────────
Diatur dalam UU No. 13 Tahun 2011 tentang Penanganan Fakir Miskin.
• Tujuan: mempercepat pengurangan kemiskinan melalui pemenuhan hak dasar, perlindungan sosial, pemberdayaan, dan kemitraan.
• Bentuk pelaksanaan: (a) bantuan pangan dan sandang; (b) penyediaan pelayanan perumahan; (c) jaminan kesehatan; (d) pendidikan dan pelatihan kerja; (e) akses modal usaha; (f) pendampingan sosial.
• Pelaksanaan dilakukan secara terpadu dan lintas sektor antara Kemensos, Kemenko PMK, Pemda, dan BUMN/Swasta.

──────────────────────────────────────
5. PENANGGUNG JAWAB & PERAN MASYARAKAT/BADAN USAHA
──────────────────────────────────────
• Pemerintah Pusat (Kemensos): menetapkan kebijakan, norma, standar, dan prosedur; mengalokasikan APBN; melakukan pengawasan (Pasal 24-25 UU 11/2009).
• Pemerintah Daerah (Dinas Sosial Kabupaten): menyelenggarakan layanan sosial di tingkat lokal sesuai urusan wajib pemerintahan daerah berdasarkan UU No. 23 Tahun 2014 tentang Pemerintahan Daerah.
• Masyarakat: berpartisipasi melalui organisasi sosial, relawan, dan Tenaga Kesejahteraan Sosial (TKS) sebagai pelaksana di lapangan (Pasal 38 UU 11/2009).
• Badan Usaha: berkontribusi melalui program CSR (Corporate Social Responsibility) sebagaimana diatur Pasal 74 UU No. 40 Tahun 2007 tentang Perseroan Terbatas.

──────────────────────────────────────
REFERENSI
──────────────────────────────────────
• UU No. 11 Tahun 2009 tentang Kesejahteraan Sosial
• UU No. 13 Tahun 2011 tentang Penanganan Fakir Miskin
• UU No. 40 Tahun 2004 tentang Sistem Jaminan Sosial Nasional
• UU No. 24 Tahun 2011 tentang BPJS
• UU No. 23 Tahun 2014 tentang Pemerintahan Daerah
• Hadjon, P. M. (2011). Pengantar Hukum Administrasi Indonesia. Gadjah Mada University Press.

Demikian analisis saya. Terima kasih.
""".strip()
},

# ══════════════════════════════════════════════════════════════════════════════
{
"matkul": "Ilmu Negara (HKUM4207) — Diskusi 8",
"isi": """
Assalamualaikum Wr. Wb. / Salam sejahtera,

Menanggapi pertanyaan diskusi terakhir yang sangat menarik ini, berikut pandangan saya berbasis analisis teoretis dan fenomena empiris.

──────────────────────────────────────
I. PEMBAGIAN KEKUASAAN (TRIAS POLITICA): SATU-SATUNYA PENJAMIN?
──────────────────────────────────────
Doktrin Trias Politica yang dicetuskan Montesquieu dalam "De l'Esprit des Lois" (1748) memisahkan kekuasaan negara menjadi tiga: legislatif (membuat UU), eksekutif (melaksanakan UU), dan yudikatif (mengadili). Tujuannya mencegah absolutisme melalui mekanisme checks and balances.

Namun, saya berpandangan bahwa Trias Politica bukanlah satu-satunya model yang dapat menjamin keberlangsungan negara, dengan alasan sebagai berikut:

Pertama, Jimly Asshiddiqie (2006) mencatat bahwa negara modern telah mengembangkan pemisahan kekuasaan menjadi enam atau bahkan delapan fungsi, meliputi fungsi pemilihan umum, audit keuangan, kejaksaan, dan bank sentral. Ini menunjukkan bahwa Trias Politica klasik sudah tidak memadai untuk menggambarkan praktik kenegaraan kontemporer.

Kedua, konstitusi Indonesia sendiri menganut pembagian kekuasaan (distribution of power), bukan pemisahan mutlak. MPR, DPR, DPD, Presiden, MA, MK, BPK, dan KY adalah lembaga-lembaga yang secara bersama menjaga keberlangsungan negara.

──────────────────────────────────────
II. STATE AUXILIARY ORGANS / QUASI ORGAN NEGARA
──────────────────────────────────────
Munculnya quasi organ negara (lembaga negara bantu) merupakan respons atas kompleksitas pemerintahan modern yang tidak dapat ditangani ketiga cabang tradisional. Contoh di Indonesia:
• KPK — pemberantasan korupsi (independen dari eksekutif)
• KPU & Bawaslu — penyelenggara pemilu netral
• Komnas HAM — pengawasan hak asasi manusia
• OJK — pengawasan sektor keuangan
• Ombudsman — pengawasan pelayanan publik

Jimly Asshiddiqie (2006) mengategorikan lembaga-lembaga ini sebagai independent regulatory agencies yang memiliki kewenangan regulasi, quasi-judisial, dan quasi-legislatif. Keberadaannya justru memperkuat, bukan melemahkan, checks and balances, karena mengisi kekosongan pengawasan yang tidak dapat dilakukan oleh tiga cabang tradisional.

──────────────────────────────────────
III. NEGARA TANPA TIGA CABANG KEKUASAAN?
──────────────────────────────────────
Secara empiris terdapat beberapa model yang berbeda:

a. Model Westminster (Inggris): tidak ada pemisahan tegas antara eksekutif dan legislatif. Perdana Menteri (eksekutif) adalah anggota parlemen (legislatif) yang memimpin mayoritas. Namun negara tetap berjalan stabil karena supremasi parlemen.

b. Tiongkok: menganut sistem kepemimpinan tunggal Partai Komunis Tiongkok dengan Kongres Rakyat Nasional sebagai lembaga tertinggi. Trias Politica tidak diterapkan, namun negara tetap berfungsi — meskipun dengan model demokrasi yang berbeda.

c. Arab Saudi: monarki absolut tanpa pemisahan kekuasaan formal; hukum Islam (syariat) menjadi konstitusi. Keberlangsungan negara dijamin oleh tradisi dan legitimasi agama.

Dari contoh-contoh tersebut, keberlangsungan negara lebih ditentukan oleh legitimasi, efektivitas pemerintahan, dan perlindungan hak rakyat, daripada oleh format formal Trias Politica.

──────────────────────────────────────
REFERENSI
──────────────────────────────────────
• Montesquieu. (1748). De l'Esprit des Lois [The Spirit of the Laws]. Geneva.
• Asshiddiqie, J. (2006). Perkembangan dan Konsolidasi Lembaga Negara Pasca Reformasi. Sekretariat Jenderal MK RI.
• Strong, C. F. (1963). Modern Political Constitutions. Sidgwick & Jackson.
• UUD Negara Republik Indonesia Tahun 1945.

Demikian pandangan saya. Saya sangat terbuka terhadap masukan dan perspektif berbeda dari rekan mahasiswa. Terima kasih.
""".strip()
},

# ══════════════════════════════════════════════════════════════════════════════
{
"matkul": "Pancasila (MKWU4110) — Diskusi 8",
"isi": """
Assalamualaikum Wr. Wb. / Salam sejahtera,

Menanggapi pertanyaan diskusi Modul 6 ini, berikut pendapat pribadi saya.

──────────────────────────────────────
KONSEKUENSI JIKA INDONESIA MENGABAIKAN PANCASILA DALAM PEMBANGUNAN
──────────────────────────────────────
Jika Indonesia sepenuhnya mengikuti model pembangunan berbasis pertumbuhan ekonomi cepat tanpa mempertimbangkan nilai-nilai Pancasila, saya berpendapat akan muncul sejumlah konsekuensi serius dalam jangka panjang.

Pertama, dari sisi keadilan sosial (Sila ke-5), pertumbuhan ekonomi yang hanya berorientasi pada angka dan investasi besar cenderung memperlebar kesenjangan antara kelompok kaya dan miskin. Eksploitasi sumber daya alam demi daya saing global akan merugikan masyarakat adat dan komunitas lokal yang hidupnya bergantung pada alam. Ketimpangan ini berpotensi memicu konflik horizontal dan instabilitas sosial.

Kedua, dari sisi persatuan (Sila ke-3), masuknya modal asing besar-besaran tanpa filter nilai kebangsaan dapat mengikis identitas budaya lokal. Westernisasi dan materialisme yang menyertai globalisasi ekonomi berpotensi melunturkan gotong royong—nilai luhur yang justru menjadi perekat kebhinekaan Indonesia.

Ketiga, dari sisi kemanusiaan (Sila ke-2), pengabaian aspek lingkungan dan HAM demi efisiensi ekonomi akan melahirkan generasi yang tercerabut dari akar kemanusiaannya, rentan terhadap dehumanisasi akibat tekanan kapital.

Pancasila sebagai paradigma pembangunan seharusnya menempatkan manusia—bukan modal—sebagai subjek pembangunan. Pembangunan yang kompetitif secara global namun berjiwa Pancasila adalah pembangunan yang mengintegrasikan pertumbuhan ekonomi dengan pemerataan kesejahteraan, pelestarian budaya, dan keberlanjutan ekologis. Konsep ini sejalan dengan Sustainable Development Goals (SDGs) yang pada dasarnya kompatibel dengan nilai-nilai Pancasila.

Singkatnya, bukan pilihan antara kompetitif atau berkarakter—Indonesia harus kompetitif karena berkarakter Pancasila.

──────────────────────────────────────
REFERENSI
──────────────────────────────────────
• Kaelan. (2013). Negara Kebangsaan Pancasila. Paradigma.
• Notonagoro. (1975). Pancasila Dasar Falsafah Negara. Pantjuran Tudjuh.
• MPR RI. (2012). Empat Pilar Kehidupan Berbangsa dan Bernegara. Sekretariat Jenderal MPR RI.
• Pembukaan UUD Negara Republik Indonesia Tahun 1945, Alinea ke-4.

Demikian pendapat saya. Saya menghargai pendapat rekan-rekan lain dan berharap diskusi ini semakin memperkaya wawasan kita bersama. Terima kasih.
""".strip()
},

# ══════════════════════════════════════════════════════════════════════════════
{
"matkul": "Pendidikan Agama Islam (MKWU4101) — Diskusi 8",
"isi": """
Assalamualaikum Wr. Wb.,

Bismillahirrahmanirrahim. Berikut pendapat saya mengenai pentingnya kerukunan antar umat beragama dalam masyarakat yang majemuk.

──────────────────────────────────────
MENGAPA KERUKUNAN ANTARUMAT BERAGAMA SANGAT PENTING?
──────────────────────────────────────
Indonesia adalah negara dengan tingkat pluralitas agama dan budaya tertinggi di dunia—memiliki enam agama yang diakui negara, ratusan kepercayaan lokal, serta lebih dari 1.340 suku bangsa. Kerukunan antarumat beragama bukan sekadar pilihan, melainkan keniscayaan untuk menjaga persatuan dan keberlangsungan NKRI.

Secara argumentatif, pentingnya kerukunan dapat dipahami dari tiga perspektif:

1. Perspektif Islam
Al-Quran Surat Al-Hujurat (49:13) menegaskan: "Hai manusia, sesungguhnya Kami menciptakan kamu dari seorang laki-laki dan seorang perempuan dan menjadikan kamu berbangsa-bangsa dan bersuku-suku supaya kamu saling kenal-mengenal." Keberagaman adalah sunnatullah (hukum alam ciptaan Allah), bukan hambatan. Islam mengenal prinsip tasamuh (toleransi), yang bukan berarti mencampuradukkan akidah, melainkan menghargai eksistensi keyakinan lain dalam bingkai ukhuwah insaniyah (persaudaraan sesama manusia).

Nabi Muhammad SAW pun mencontohkan kerukunan dalam Piagam Madinah (622 M), di mana beliau menjamin hak-hak warga non-Muslim untuk beribadah dan mempertahankan agama mereka selama menjunjung perdamaian bersama.

2. Perspektif Sosial-Kemasyarakatan
Kerukunan adalah fondasi stabilitas sosial. Konflik berbasis agama, seperti yang pernah terjadi di Ambon (1999-2002) atau Poso (1998-2001), membuktikan betapa rusaknya tatanan sosial, ekonomi, dan kehidupan masyarakat ketika kerukunan hancur. Sebaliknya, daerah-daerah yang mampu menjaga toleransi justru lebih maju secara sosial dan ekonomi.

3. Perspektif Berbangsa dan Bernegara
Bhinneka Tunggal Ika bukan sekadar semboyan, melainkan kontrak sosial bangsa Indonesia. Sila Pertama Pancasila, "Ketuhanan Yang Maha Esa," tidak hanya menjamin kebebasan beragama, tetapi juga mewajibkan setiap warga negara menghormati pemeluk agama lain (UU No. 39/1999 tentang HAM, Pasal 22).

──────────────────────────────────────
CONTOH KONKRET UPAYA MEMBANGUN KERUKUNAN SAAT INI
──────────────────────────────────────
• Forum Kerukunan Umat Beragama (FKUB) di setiap kabupaten/kota: forum dialog lintas agama yang mempertemukan tokoh-tokoh agama untuk menyelesaikan potensi konflik secara musyawarah.
• Program "Rumah Moderasi Beragama" di kampus-kampus PTKIN yang mendorong mahasiswa untuk menjadi agen moderasi dan toleransi.
• Kegiatan bakti sosial lintas agama (seperti di NTT—mayoritas Katolik namun hidup damai bersama Muslim)—contoh nyata bahwa perbedaan tidak menghalangi kerja sama kemanusiaan.
• Gerakan #BersamaJagaRukunah di media sosial yang menangkal narasi kebencian dengan konten perdamaian.

Kerukunan sejati bukan berarti semua agama sama, tetapi semua manusia sama-sama berhak hidup damai dan bermartabat. Itulah esensi rahmatan lil 'alamin yang diajarkan Islam.

──────────────────────────────────────
REFERENSI
──────────────────────────────────────
• Al-Quran, QS. Al-Hujurat (49:13); QS. Al-Kafirun (109:1-6).
• Piagam Madinah (622 M) — dokumen toleransi pertama dalam sejarah Islam.
• UU No. 39 Tahun 1999 tentang Hak Asasi Manusia, Pasal 22.
• Surat Keputusan Bersama (SKB) 3 Menteri No. 3/2008 tentang Kerukunan Umat Beragama.
• Shihab, M. Q. (2000). Wawasan Al-Quran. Mizan.

Wassalamualaikum Wr. Wb. Terima kasih atas perhatiannya.
""".strip()
},

# ══════════════════════════════════════════════════════════════════════════════
{
"matkul": "Pendidikan Kewarganegaraan / PKN (MKWU4109) — Diskusi 8",
"isi": """
Assalamualaikum Wr. Wb. / Salam sejahtera,

Berikut pandangan saya mengenai ketahanan nasional Indonesia dalam menghadapi globalisasi, ancaman siber, dan konflik regional.

──────────────────────────────────────
1. PENGARUH GLOBALISASI TERHADAP KETAHANAN NASIONAL INDONESIA
──────────────────────────────────────
Globalisasi adalah proses integrasi dunia dalam bidang ekonomi, politik, sosial, budaya, dan teknologi yang melampaui batas-batas negara. Dalam konteks ketahanan nasional yang menggunakan pendekatan Astagatra (Trigatra: geografi, SDA, demografi + Pancagatra: ideologi, politik, ekonomi, sosial-budaya, hankam), globalisasi memiliki dampak ganda.

DAMPAK POSITIF:
• Ekonomi: Indonesia mendapat akses pasar ekspor yang lebih luas, masuknya investasi asing, dan transfer teknologi yang mendorong produktivitas nasional. Bergabungnya Indonesia dalam ASEAN, G20, dan WTO meningkatkan daya tawar diplomatik dan ekonomi.
• Iptek: Globalisasi mempercepat difusi teknologi—termasuk teknologi pertahanan—yang memperkuat kapabilitas militer dan kemanan nasional (Gatra hankam).
• Demokrasi: Tekanan komunitas internasional mendorong perbaikan tata kelola pemerintahan, penegakan HAM, dan transparansi (Gatra politik).

DAMPAK NEGATIF:
• Ideologi: Masuknya liberalisme, sekularisme, dan radikalisme transnasional mengancam Pancasila sebagai ideologi bangsa. Polarisasi berbasis SARA mengikis persatuan (Gatra ideologi).
• Ekonomi: Dominasi modal asing dan produk impor dapat mematikan industri lokal dan memperlebar ketimpangan ekonomi (Gatra ekonomi).
• Sosial-Budaya: Westernisasi mengancam nilai-nilai lokal, gotong royong, dan identitas kebangsaan (Gatra sosbudaya).
• Keamanan: Globalisasi memudahkan peredaran narkoba transnasional, perdagangan manusia (TPPO), terorisme lintas batas, dan kejahatan siber (Gatra hankam).

──────────────────────────────────────
2. UPAYA PEMERINTAH MENGHADAPI ANCAMAN SIBER & KONFLIK REGIONAL
──────────────────────────────────────
A. Ancaman Siber:
• Pembentukan Badan Siber dan Sandi Negara (BSSN) melalui Perpres No. 28 Tahun 2021 sebagai lembaga khusus keamanan siber nasional.
• Penerbitan Peraturan Pemerintah No. 71 Tahun 2019 tentang Penyelenggaraan Sistem dan Transaksi Elektronik (PSTE) yang mengatur keamanan data dan sistem elektronik nasional.
• Pembangunan Security Operations Center (SOC) di instansi-instansi kritis negara untuk mendeteksi dan merespons serangan siber secara real-time.
• Kerja sama bilateral dan multilateral dalam bidang keamanan siber, termasuk dengan ASEAN Cybersecurity Cooperation Strategy.
• Program literasi digital nasional melalui Gerakan Nasional Literasi Digital (GNLD) Kominfo untuk meningkatkan kewaspadaan masyarakat terhadap hoaks, phishing, dan manipulasi siber.

B. Konflik Regional:
• Indonesia mengedepankan pendekatan diplomasi aktif sesuai politik luar negeri bebas-aktif berdasarkan Pasal 11 UUD 1945. Contoh: peran Indonesia sebagai mediator dalam konflik Myanmar melalui konsensus 5 poin ASEAN (2021).
• Modernisasi alutsista TNI berdasarkan Minimum Essential Force (MEF) dalam Renstra Kemenhan untuk meningkatkan daya tangkal (deterrence) dari potensi konflik.
• Keikutsertaan aktif dalam misi perdamaian PBB (Kontingen Garuda) sebagai instrumen diplomasi pertahanan sekaligus membangun kepercayaan internasional.
• Penguatan kerja sama maritim di Laut Natuna Utara melalui patroli gabungan TNI AL dan penegasan kedaulatan NKRI dari klaim ilegal negara lain.

──────────────────────────────────────
REFERENSI
──────────────────────────────────────
• UU No. 3 Tahun 2002 tentang Pertahanan Negara.
• Perpres No. 28 Tahun 2021 tentang BSSN.
• PP No. 71 Tahun 2019 tentang PSTE.
• Lemhannas RI. (2022). Modul Ketahanan Nasional. Lembaga Ketahanan Nasional.
• Suradinata, E. (2005). Geopolitik dan Geostrategi Indonesia. Lembaga Pengkajian dan Pengembangan Kehidupan Bernegara.

Demikian pandangan saya. Semoga bermanfaat. Terima kasih.
""".strip()
},

# ══════════════════════════════════════════════════════════════════════════════
{
"matkul": "Pengantar Ilmu Hukum (HKUM4101) — Diskusi 8",
"isi": """
Assalamualaikum Wr. Wb. / Salam sejahtera,

Saya akan memberikan argumen saya mengenai topik "Trias Politica" disertai contoh konkret dan rujukan ilmiah.

──────────────────────────────────────
TRIAS POLITICA: FONDASI NEGARA HUKUM DEMOKRATIS
──────────────────────────────────────
Trias Politica adalah doktrin pemisahan kekuasaan negara menjadi tiga fungsi: legislatif (membentuk undang-undang), eksekutif (melaksanakan undang-undang), dan yudikatif (mengadili pelanggaran hukum). Doktrin ini pertama kali dikembangkan secara sistematis oleh Montesquieu dalam karyanya "De l'Esprit des Lois" (1748), meskipun benih pemikirannya telah ada sejak John Locke dalam "Two Treatises of Government" (1689).

ARGUMEN UTAMA: Trias Politica adalah mekanisme esensial untuk mencegah penyalahgunaan kekuasaan dan menjamin kebebasan warga negara.

Montesquieu berargumen: "Lorsque dans la même personne ou dans le même corps de magistrature, la puissance législative est réunie à la puissance exécutrice, il n'y a point de liberté" — bahwa apabila kekuasaan legislatif dan eksekutif berada di tangan yang sama, tidak ada kebebasan yang dapat terjamin (Montesquieu, 1748, Buku XI).

──────────────────────────────────────
TRIAS POLITICA DI INDONESIA
──────────────────────────────────────
Indonesia mengadopsi prinsip Trias Politica namun dengan model checks and balances yang lebih kompleks pasca-amendemen UUD 1945 (1999–2002). Kekuasaan tidak dipisahkan secara mutlak, tetapi dibagi (distribution of power) di antara:
• Legislatif: MPR (DPR + DPD) — membentuk UU, menetapkan APBN, mengawasi eksekutif.
• Eksekutif: Presiden — menjalankan pemerintahan, mengeluarkan Perpres/PP.
• Yudikatif: MA (peradilan umum, agama, militer, TUN) dan MK (uji konstitusionalitas UU).

Contoh konkret checks and balances:
• MK membatalkan sejumlah pasal dalam UU Cipta Kerja (Putusan MK No. 91/PUU-XVIII/2020) karena dinyatakan inkonstitusional bersyarat — ini adalah yudikatif mengontrol legislatif dan eksekutif.
• DPR menolak RUU yang diajukan Presiden, atau melalui hak angket menyelidiki kebijakan eksekutif — ini adalah legislatif mengontrol eksekutif.

──────────────────────────────────────
KELEBIHAN DAN KELEMAHAN TRIAS POLITICA
──────────────────────────────────────
Kelebihan:
• Mencegah tirani dan absolutisme kekuasaan.
• Menjamin perlindungan hak-hak warga negara.
• Menciptakan akuntabilitas dan transparansi pemerintahan.

Kelemahan:
• Dapat menimbulkan deadlock antarcabang (gridlock), seperti sering terjadi di Amerika Serikat antara Congress dan Presiden.
• Dalam praktik, batas pemisahan kekuasaan tidak selalu tegas—eksekutif sering memiliki kewenangan legislatif melalui peraturan delegasi.

──────────────────────────────────────
KESIMPULAN
──────────────────────────────────────
Trias Politica tetap relevan sebagai kerangka dasar negara demokratis karena menyediakan mekanisme saling mengawasi yang mencegah konsentrasi kekuasaan. Namun, dalam perkembangannya, Trias Politica telah berevolusi melalui hadirnya lembaga-lembaga independen (KPK, KPU, OJK, Komnas HAM) yang memperkaya sistem checks and balances melampaui tiga cabang klasik.

──────────────────────────────────────
REFERENSI
──────────────────────────────────────
• Montesquieu. (1748). De l'Esprit des Lois. Geneva: Barillot & Fils.
• Locke, J. (1689). Two Treatises of Government. London: Awnsham Churchill.
• Asshiddiqie, J. (2010). Pengantar Ilmu Hukum Tata Negara. Rajawali Pers.
• Putusan MK No. 91/PUU-XVIII/2020 tentang UU Cipta Kerja.
• UUD Negara Republik Indonesia Tahun 1945.

Demikian argumen saya. Terima kasih atas diskusi yang sangat edukatif ini.
""".strip()
},

# ══════════════════════════════════════════════════════════════════════════════
{
"matkul": "Sistem Hukum Indonesia (HKUM4201) — Diskusi 8",
"isi": """
Assalamualaikum Wr. Wb. / Salam sejahtera,

Berikut saya uraikan proses/tahapan perjanjian internasional antar negara disertai landasan hukum dan teori yang relevan.

──────────────────────────────────────
DASAR HUKUM
──────────────────────────────────────
• Internasional: Vienna Convention on the Law of Treaties (VCLT) 1969 — instrumen utama hukum perjanjian internasional, berlaku sejak 1980.
• Nasional: UU No. 24 Tahun 2000 tentang Perjanjian Internasional — mengatur prosedur Indonesia dalam mengikatkan diri pada perjanjian internasional.
• Konstitusional: Pasal 11 UUD 1945 — Presiden mempunyai kewenangan membuat perjanjian internasional dengan persetujuan DPR (untuk perjanjian tertentu).

──────────────────────────────────────
TEORI YANG RELEVAN
──────────────────────────────────────
• Teori Pacta Sunt Servanda (Pasal 26 VCLT): setiap perjanjian yang berlaku mengikat para pihak dan harus dilaksanakan dengan itikad baik (good faith). Ini adalah prinsip fundamental hukum perjanjian internasional.
• Teori Dualisme (Triepel, Anzilotti): hukum internasional dan hukum nasional adalah dua sistem yang terpisah; perjanjian internasional baru berlaku di dalam negeri setelah diratifikasi melalui peraturan perundang-undangan nasional — pendekatan yang dianut Indonesia.
• Teori Kehendak Negara (Voluntarism): negara hanya terikat pada perjanjian yang secara sukarela dan bebas telah disetujuinya.

──────────────────────────────────────
TAHAPAN PERJANJIAN INTERNASIONAL
──────────────────────────────────────
Berdasarkan VCLT 1969 dan UU No. 24 Tahun 2000, terdapat lima tahapan utama:

TAHAP 1 — PERUNDINGAN (Negotiation)
Negara-negara yang berkepentingan melakukan negosiasi melalui delegasi resmi (biasanya Menteri Luar Negeri atau pejabat yang diberi full powers/surat kuasa penuh). Dalam sistem Indonesia, Menlu atau pejabat yang ditunjuk Presiden memimpin perundingan. Dalam tahap ini dibahas isi (materi) perjanjian, hak, kewajiban, dan mekanisme penyelesaian sengketa.

TAHAP 2 — PERUMUSAN NASKAH (Adoption of the Text)
Setelah negosiasi, delegasi merumuskan teks perjanjian yang disepakati bersama. Penerimaan teks (adoption) dalam konferensi internasional umumnya memerlukan suara dua pertiga peserta kecuali disepakati lain (Pasal 9 VCLT).

TAHAP 3 — AUTENTIKASI / PENANDATANGANAN (Authentication/Signature)
Teks yang telah dirumuskan diautentikasi—biasanya melalui penandatanganan, paraf (initialling), atau prosedur lain yang disepakati (Pasal 10 VCLT). Penandatanganan belum berarti perjanjian berlaku mengikat, tetapi negara yang telah menandatangani berkewajiban tidak melakukan tindakan yang bertentangan dengan objek dan tujuan perjanjian (Pasal 18 VCLT).

TAHAP 4 — RATIFIKASI / PENGESAHAN (Ratification/Acceptance)
Ini adalah tahap kritis: negara secara resmi menyatakan terikat pada perjanjian melalui prosedur konstitusional dalam negerinya. Di Indonesia:
• Perjanjian yang memerlukan persetujuan DPR (Pasal 11 UUD 1945 & Pasal 10 UU 24/2000): menyangkut masalah politik, perdamaian, pertahanan, perubahan wilayah, keuangan negara, dan pembuatan UU baru.
• Perjanjian yang cukup dengan Keputusan Presiden: perjanjian teknis dan administratif yang tidak termasuk kategori di atas.
Instrumen ratifikasi kemudian dipertukarkan atau diserahkan kepada depositary.

TAHAP 5 — BERLAKUNYA PERJANJIAN (Entry into Force)
Perjanjian mulai berlaku sesuai ketentuan yang termuat dalam perjanjian itu sendiri, misalnya setelah sejumlah negara tertentu meratifikasi, atau pada tanggal tertentu setelah ratifikasi terakhir (Pasal 24 VCLT).

TAHAP TAMBAHAN — PENDAFTARAN & PENGUMUMAN
Pasal 102 Piagam PBB mewajibkan perjanjian internasional yang dibuat anggota PBB untuk didaftarkan kepada Sekretariat PBB. Di Indonesia, naskah perjanjian yang telah diratifikasi diundangkan dalam Lembaran Negara RI (Pasal 15 UU 24/2000).

──────────────────────────────────────
CONTOH KONKRET
──────────────────────────────────────
Indonesia meratifikasi Paris Agreement on Climate Change (2016) melalui UU No. 16 Tahun 2016. Proses ini melalui seluruh tahapan: negosiasi di COP21 Paris (2015), penandatanganan (April 2016), pengesahan DPR, dan diundangkan dalam Lembaran Negara — sebagai contoh nyata penerapan tahapan perjanjian internasional di Indonesia.

──────────────────────────────────────
REFERENSI
──────────────────────────────────────
• Vienna Convention on the Law of Treaties (VCLT) 1969, terutama Pasal 7, 9, 10, 18, 24, 26.
• UU No. 24 Tahun 2000 tentang Perjanjian Internasional.
• Pasal 11 UUD Negara Republik Indonesia Tahun 1945.
• UU No. 16 Tahun 2016 tentang Pengesahan Paris Agreement.
• Starke, J. G. (1992). Pengantar Hukum Internasional, Jilid 1 & 2 (terjemahan). Sinar Grafika.
• Kusumaatmadja, M. & Agoes, E. R. (2010). Pengantar Hukum Internasional. Alumni.

Demikian uraian saya mengenai tahapan perjanjian internasional. Semoga bermanfaat dan saya sangat terbuka untuk berdiskusi lebih lanjut. Terima kasih.
""".strip()
},

]  # end DISKUSI list


# ─── Buat dokumen Word ────────────────────────────────────────────────────────

def set_cell_bg(cell, hex_color):
    tc   = cell._tc
    tcPr = tc.get_or_add_tcPr()
    shd  = OxmlElement("w:shd")
    shd.set(qn("w:val"),   "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"),  hex_color)
    tcPr.append(shd)


def add_heading(doc, text, level=1, color="003087"):
    p  = doc.add_paragraph()
    run = p.add_run(text)
    run.bold = True
    run.font.size = Pt(14 if level == 1 else 11)
    run.font.color.rgb = RGBColor.from_string(color)
    p.paragraph_format.space_before = Pt(12)
    p.paragraph_format.space_after  = Pt(4)
    return p


def build_doc():
    doc = Document()

    # Margin
    for section in doc.sections:
        section.top_margin    = Cm(2)
        section.bottom_margin = Cm(2)
        section.left_margin   = Cm(2.5)
        section.right_margin  = Cm(2.5)

    # Halaman cover
    doc.add_paragraph()
    t = doc.add_table(rows=1, cols=1)
    t.style = "Table Grid"
    cell = t.rows[0].cells[0]
    set_cell_bg(cell, "003087")
    p = cell.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = p.add_run("UNIVERSITAS TERBUKA\nS1 ILMU HUKUM\n\nJAWABAN DISKUSI 8\nSEMUA MATA KULIAH")
    r.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)
    r.font.size = Pt(16)

    doc.add_paragraph()
    doc.add_paragraph("IDENTITAS MAHASISWA", style="Heading 2")
    id_tbl = doc.add_table(rows=4, cols=2)
    id_tbl.style = "Table Grid"
    labels = ["Nama Lengkap", "NIM", "Program Studi", "Semester"]
    values = ["[NAMA LENGKAP]", "[NIM]", "S1 Ilmu Hukum", "1 / 2"]
    for i, (lbl, val) in enumerate(zip(labels, values)):
        id_tbl.rows[i].cells[0].text = lbl
        id_tbl.rows[i].cells[1].text = val
        id_tbl.rows[i].cells[0].paragraphs[0].runs[0].bold = True
    doc.add_paragraph()

    # Satu bagian per matkul
    for item in DISKUSI:
        doc.add_page_break()

        # Header matkul
        tbl = doc.add_table(rows=1, cols=1)
        tbl.style = "Table Grid"
        c = tbl.rows[0].cells[0]
        set_cell_bg(c, "003087")
        p = c.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(item["matkul"])
        r.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)
        r.font.size = Pt(13)

        doc.add_paragraph()

        # Isi jawaban — pisahkan per baris
        lines = item["isi"].split("\n")
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("──────"):
                p = doc.add_paragraph()
                p.paragraph_format.space_before = Pt(6)
                p.paragraph_format.space_after  = Pt(2)
                run = p.add_run("─" * 50)
                run.font.color.rgb = RGBColor(0, 48, 135)
            elif (stripped.isupper() and len(stripped) > 5 and
                  not stripped.startswith("•") and not stripped.startswith("No")):
                p = doc.add_paragraph()
                run = p.add_run(stripped)
                run.bold = True
                run.font.size = Pt(10)
                run.font.color.rgb = RGBColor(0, 48, 135)
                p.paragraph_format.space_before = Pt(6)
            elif stripped.startswith("•") or stripped.startswith("No |"):
                p = doc.add_paragraph(style="List Bullet")
                p.add_run(stripped.lstrip("• "))
                p.paragraph_format.left_indent = Cm(0.5)
            elif stripped == "":
                doc.add_paragraph()
            else:
                p = doc.add_paragraph()
                p.add_run(stripped)
                p.paragraph_format.space_after = Pt(2)

    doc.save(OUTPUT)
    print(f"Word saved: {OUTPUT}")


if __name__ == "__main__":
    build_doc()
