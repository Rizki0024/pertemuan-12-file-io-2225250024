# ============================================
# PROGRAM MENANGANI FILE TIDAK DITEMUKAN
# Judul Awal: File Not Found
# Judul Hasil: Penanganan File Hilang
# ============================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul():
    garis = "=" * 40
    judul = "LATIHAN 5 - FILE NOT FOUND"

    print(garis)
    print(judul.center(40))
    print(garis)


# Menampilkan judul program
tampilkan_judul()

# Mencoba membuka file yang tidak tersedia
try:

    # Membuka file dengan mode membaca
    with open("data/tidak_ada.txt", "r", encoding="utf-8") as file:

        # Membaca isi file
        print(file.read())

# Menangani error jika file tidak ditemukan
except FileNotFoundError:

    # Menampilkan pesan error yang mudah dipahami
    print("File tidak ditemukan.")