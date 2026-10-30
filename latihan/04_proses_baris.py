# ============================================
# PROGRAM MEMPROSES BARIS DATA
# Judul Awal: Proses Baris
# Judul Hasil: Menampilkan Data Nilai
# ============================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul():
    garis = "=" * 40
    judul = "LATIHAN 4 - PROSES BARIS"

    print(garis)
    print(judul.center(40))
    print(garis)


# Menampilkan judul program
tampilkan_judul()

# Membuka file nilai.txt dengan mode membaca
with open("data/nilai.txt", "r", encoding="utf-8") as file:

    # Membaca setiap baris dalam file
    for baris in file:

        # Menghilangkan spasi dan newline
        baris = baris.strip()

        # Melewati baris yang kosong
        if not baris:
            continue

        # Memisahkan NIM dan nilai berdasarkan koma
        nim, teks_nilai = baris.split(",")

        # Mengubah nilai dari teks menjadi angka
        nilai = float(teks_nilai)

        # Menampilkan NIM dan nilai
        print(nim, nilai)