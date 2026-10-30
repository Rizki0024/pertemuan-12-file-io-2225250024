# ============================================
# PROGRAM MEMBACA FILE
# Judul Awal: Membaca File
# Judul Hasil: Menampilkan Isi Catatan
# ============================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul():
    garis = "=" * 40
    judul = "LATIHAN 2 - MEMBACA FILE"

    print(garis)
    print(judul.center(40))
    print(garis)


# Menampilkan judul program
tampilkan_judul()

# Membuka file dengan mode r untuk membaca
with open("data/catatan.txt", "r", encoding="utf-8") as file:

    # Membaca file baris demi baris
    for baris in file:

        # strip() menghilangkan karakter newline
        print(baris.strip())
        