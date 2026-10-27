
# Sistem Data Mahasiswa - Pertemuan 11

Repositori ini berisi pengerjaan Latihan 2 mata kuliah
Algoritma dan Pemrograman, Program Studi S1 Pendidikan Matematika.

## Identitas Mahasiswa

- **Nama:** Aulia Nurrizqi
- **NIM:** 2225250160
- **Kelas:** 3A
- **Materi:** Dictionary/Map dan Pasangan Key-Value dalam Python

## Tujuan

Membuat program Python untuk mengelola data mahasiswa menggunakan
struktur data dictionary dengan NIM sebagai key utama.

## Struktur Data

Data mahasiswa disimpan menggunakan dictionary bersarang.

Setiap NIM menjadi key utama, sedangkan value berisi:
- `nama`: nama mahasiswa
- `kelas`: kelas mahasiswa
- `nilai`: nilai mahasiswa

Contoh:

```python
data_mahasiswa = {
    "A001": {
        "nama": "Ayu",
        "kelas": "A",
        "nilai": 85
    }
}
```

## Fitur Program

1. Mencari data mahasiswa berdasarkan NIM.
2. Menampilkan pesan jika data tidak ditemukan.
3. Menambahkan mahasiswa baru.
4. Mengubah nilai mahasiswa.
5. Menampilkan seluruh data menggunakan `items()`.
6. Menghitung rata-rata nilai seluruh mahasiswa.
7. Menggunakan fungsi untuk pencarian dan perhitungan rata-rata.

## Struktur Folder

```text
pertemuan-11-dictionary-NIM/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_dasar_dictionary.py
│   ├── 02_akses_get.py
│   ├── 03_manipulasi_dictionary.py
│   ├── 04_iterasi_dictionary.py
│   ├── 05_dictionary_bersarang.py
│   └── 06_fungsi_dictionary.py
└── praktik/
    └── data_mahasiswa.py
```

## Cara Menjalankan Program

Pastikan Python 3 sudah terpasang.

Jalankan perintah berikut melalui terminal VS Code dari
folder utama proyek:

```bash
python praktik/data_mahasiswa.py
```

Jika menggunakan Python 3 dengan perintah berbeda, jalankan:

```bash
python3 praktik/data_mahasiswa.py
```

## Pengujian Program

| No. | Pengujian | Hasil |
|---|---|---|
| 1 | Mencari NIM A003 | Data Citra ditemukan |
| 2 | Mencari NIM A999 | Data tidak ditemukan |
| 3 | Menambahkan NIM A006 | Mahasiswa baru berhasil ditambahkan |
| 4 | Mengubah nilai A002 menjadi 82 | Nilai Budi berubah menjadi 82 |
| 5 | Menampilkan rekap data | Seluruh data mahasiswa ditampilkan |
| 6 | Menghitung rata-rata | Rata-rata nilai ditampilkan |

**Catatan:** Hasil pengujian aktual perlu diperiksa dengan
menjalankan program di VS Code.

## Konsep yang Dipelajari

- Dictionary dan pasangan key-value.
- Penggunaan `get()` untuk akses data yang aman.
- Penambahan dan perubahan data dictionary.
- Perulangan menggunakan `items()` dan `values()`.
- Pembuatan fungsi dalam Python.
- Pengolahan data mahasiswa dan perhitungan rata-rata.

## Refleksi

Dictionary memudahkan pencarian data mahasiswa karena NIM
digunakan sebagai key utama. Penggunaan `get()` membantu
menghindari kesalahan ketika data tidak ditemukan.
Sementara itu, `items()` memudahkan penelusuran seluruh data
dan fungsi membuat program lebih terstruktur.


Program ini dibuat untuk memenuhi kebutuhan pembelajaran
Algoritma dan Pemrograman.
