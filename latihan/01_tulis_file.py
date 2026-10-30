# ============================================
# PROGRAM MENULIS FILE
# Judul Awal: Menulis File
# Judul Hasil: Membuat Catatan Pertemuan 12
# ============================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul():
    garis = "=" * 40
    judul = "LATIHAN 1 - MENULIS FILE"

    print(garis)
    print(judul.center(40))
    print(garis)


# Menampilkan judul program
tampilkan_judul()

# Membuka file dengan mode w untuk menulis
# Jika file belum ada, Python akan membuatnya
with open("data/catatan.txt", "w", encoding="utf-8") as file:

    # Menulis teks pertama ke dalam file
    file.write("Algoritma dan Pemrograman\n")

    # Menulis teks kedua ke dalam file
    file.write("Pertemuan 12\n")

# Menampilkan pesan bahwa proses berhasil
print("Data berhasil ditulis ke file catatan.txt")