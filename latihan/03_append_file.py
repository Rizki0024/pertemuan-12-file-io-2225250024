# ============================================
# PROGRAM MENAMBAHKAN ISI FILE
# Judul Awal: Append File
# Judul Hasil: Menambahkan Catatan
# ============================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul():
    garis = "=" * 40
    judul = "LATIHAN 3 - APPEND FILE"

    print(garis)
    print(judul.center(40))
    print(garis)


# Menampilkan judul program
tampilkan_judul()

# Membuka file dengan mode a untuk menambahkan data
with open("data/catatan.txt", "a", encoding="utf-8") as file:

    # Menambahkan teks di akhir file
    file.write("Latihan append berhasil.\n")

# Menampilkan pesan berhasil
print("Data berhasil ditambahkan ke file.")