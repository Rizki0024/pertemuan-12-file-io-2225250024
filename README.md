# Pertemuan 12 - File I/O dan Error Handling

Nama: ...
NIM: ...
Kelas: ...

## Tujuan

Mempelajari cara membaca, menulis, dan mengolah data menggunakan file
di Python serta menangani error dasar menggunakan try-except.

## Materi yang Dipelajari

1. Membuka file menggunakan open() dan with.
2. Menggunakan mode r, w, dan a.
3. Membaca file menggunakan read(), readline(), dan readlines().
4. Menulis dan menambahkan data ke file.
5. Mengolah data menggunakan strip(), split(), dan float().
6. Menangani FileNotFoundError dan ValueError.
7. Membuat fungsi untuk membaca dan menulis file.

## Struktur Folder

pertemuan-12-file-io-NIM/
- README.md
- .gitignore
- data/
  - catatan.txt
  - nilai.txt
  - hasil_rekap.txt
- latihan/
  - 01_tulis_file.py
  - 02_baca_file.py
  - 03_append_file.py
  - 04_proses_baris.py
  - 05_file_not_found.py
  - 06_value_error.py
- tugas/
  - rekap_nilai_file.py
- kuis_formatif.md

## Format File Input

File data/nilai.txt menggunakan format:

NIM,nilai

Contoh:

A001,85
A002,78
A003,92
A004,abc
A005,74
A006,88

Baris A004,abc digunakan untuk menguji penanganan data yang tidak valid.

## Cara Menjalankan

Jalankan terminal dari folder utama proyek.

Untuk menjalankan latihan:

python latihan/01_tulis_file.py
python latihan/02_baca_file.py
python latihan/03_append_file.py
python latihan/04_proses_baris.py
python latihan/05_file_not_found.py
python latihan/06_value_error.py

Untuk menjalankan tugas utama:

python tugas/rekap_nilai_file.py

## Hasil Tugas

Program membaca data dari data/nilai.txt, melewati baris kosong,
menangani data yang tidak valid, menghitung statistik nilai,
dan menyimpan hasilnya ke data/hasil_rekap.txt.

Hasil pengolahan data contoh:

- Jumlah data valid: 5
- Rata-rata: 83.40
- Minimum: 74.00
- Maksimum: 92.00
- Jumlah lulus: 5

## Test Case

| Kasus | Kondisi | Hasil yang Diharapkan |
|---|---|---|
| Normal | Semua baris valid | Semua data diproses |
| File hilang | File nilai.txt tidak tersedia | Pesan file tidak ditemukan |
| Nilai invalid | A004,abc | Baris dilewati, data lain tetap diproses |
| Baris kosong | Terdapat baris kosong | Baris kosong dilewati |
| Batas lulus | Nilai 60 | Dihitung sebagai lulus |

## Error yang Ditangani

- FileNotFoundError: ketika file input tidak ditemukan.
- ValueError: ketika format data atau konversi nilai tidak valid.

## Refleksi

Pada pertemuan ini saya mempelajari cara menyimpan dan membaca data
menggunakan file sehingga data tidak hanya tersimpan selama program
berjalan. Saya juga mempelajari penggunaan mode r, w, dan a serta
penanganan error menggunakan try-except.

Salah satu error yang ditemukan adalah ValueError ketika program
membaca nilai yang berisi teks, seperti A004,abc. Program dapat
melewati baris tersebut sehingga data valid lainnya tetap diproses.

## Sumber dan Bantuan

- Bahan Ajar Algoritma dan Pemrograman Pertemuan 12.
- Dokumentasi Python.
- Bantuan ChatGPT untuk memahami materi, menyusun contoh kode,
  dan memeriksa alur pengerjaan.