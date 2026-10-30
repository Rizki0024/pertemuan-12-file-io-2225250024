# ==================================================
# PROGRAM TUGAS 5 - REKAP NILAI DARI FILE
# Judul Awal: Rekap Nilai dari File
# Judul Hasil: Sistem Pengolahan Data Nilai Mahasiswa
# ==================================================

# Fungsi untuk menampilkan judul program
def tampilkan_judul():
    garis = "=" * 50
    judul = "TUGAS 5 - REKAP NILAI DARI FILE"

    print(garis)
    print(judul.center(50))
    print(garis)


# Fungsi untuk membaca dan memvalidasi data
def baca_data(nama_file):

    # Menyiapkan list untuk menyimpan data yang valid
    data = []

    # Mencoba membuka file input
    try:
        with open(nama_file, "r", encoding="utf-8") as file:

            # Membaca setiap baris dengan nomor baris
            for nomor, baris in enumerate(file, start=1):

                # Membersihkan baris dari spasi dan newline
                baris = baris.strip()

                # Melewati baris kosong
                if not baris:
                    continue

                # Mencoba memisahkan NIM dan nilai
                try:
                    nim, teks_nilai = baris.split(",")

                    # Mengubah nilai teks menjadi float
                    nilai = float(teks_nilai)

                    # Menyimpan data valid sebagai tuple
                    data.append((nim.strip(), nilai))

                # Menangani format baris atau nilai yang tidak valid
                except ValueError:
                    print(f"Baris {nomor} dilewati: {baris}")

    # Menangani jika file input tidak ditemukan
    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    # Mengembalikan seluruh data yang valid
    return data


# Fungsi untuk menghitung dan menulis rekap
def tulis_rekap(nama_file, data):

    # Memeriksa apakah terdapat data valid
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    # Menyiapkan list untuk menyimpan nilai
    nilai = []

    # Mengambil nilai dari setiap record
    for item in data:
        nilai.append(item[1])

    # Menghitung jumlah data valid
    jumlah_data = len(nilai)

    # Menghitung rata-rata nilai
    rata_rata = sum(nilai) / jumlah_data

    # Mencari nilai minimum
    nilai_minimum = min(nilai)

    # Mencari nilai maksimum
    nilai_maksimum = max(nilai)

    # Menghitung jumlah mahasiswa yang lulus
    # Nilai minimal untuk lulus adalah 60
    jumlah_lulus = 0

    for angka in nilai:
        if angka >= 60:
            jumlah_lulus += 1

    # Membuka file output dengan mode w
    with open(nama_file, "w", encoding="utf-8") as file:

        # Menulis jumlah data valid
        file.write(f"Jumlah data valid: {jumlah_data}\n")

        # Menulis rata-rata nilai
        file.write(f"Rata-rata: {rata_rata:.2f}\n")

        # Menulis nilai minimum
        file.write(f"Minimum: {nilai_minimum:.2f}\n")

        # Menulis nilai maksimum
        file.write(f"Maksimum: {nilai_maksimum:.2f}\n")

        # Menulis jumlah mahasiswa yang lulus
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")


# ============================================
# ALUR UTAMA PROGRAM
# ============================================

# Menampilkan judul program
tampilkan_judul()

# Menentukan lokasi file input
input_file = "data/nilai.txt"

# Menentukan lokasi file output
output_file = "data/hasil_rekap.txt"

# Memanggil fungsi untuk membaca data
data = baca_data(input_file)

# Memeriksa apakah terdapat data valid
if data:

    # Memanggil fungsi untuk menulis hasil rekap
    tulis_rekap(output_file, data)

    # Menampilkan informasi jumlah data yang berhasil diproses
    print(f"Jumlah data valid: {len(data)}")

    # Menampilkan pesan keberhasilan
    print(f"Rekap berhasil ditulis ke {output_file}")

else:

    # Menampilkan pesan jika tidak ada data yang dapat diproses
    print("Proses rekap tidak dapat dilanjutkan.")