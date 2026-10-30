# ============================================
# PROGRAM MENANGANI VALUE ERROR
# Judul Awal: Value Error
# Judul Hasil: Validasi Input Nilai
# ============================================

# Fungsi untuk menampilkan judul di terminal
def tampilkan_judul():
    garis = "=" * 40
    judul = "LATIHAN 6 - VALUE ERROR"

    print(garis)
    print(judul.center(40))
    print(garis)


# Menampilkan judul program
tampilkan_judul()

# Meminta pengguna memasukkan nilai
teks = input("Masukkan nilai: ")

# Mencoba mengubah input menjadi angka
try:

    # Mengubah teks menjadi tipe float
    nilai = float(teks)

    # Menampilkan hasil konversi
    print(f"Nilai = {nilai}")

# Menangani error jika input bukan angka
except ValueError:

    # Menampilkan pesan jika konversi gagal
    print("Input harus berupa angka.")