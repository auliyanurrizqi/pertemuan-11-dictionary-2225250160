
# Latihan 2 - Sistem Data Mahasiswa
# Mata Kuliah: Algoritma dan Pemrograman
# Materi: Dictionary/Map dan Key-Value

def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM."""
    return data.get(nim)


def rata_rata_nilai(data):
    """Menghitung rata-rata nilai seluruh mahasiswa."""
    if len(data) == 0:
        return 0

    total = 0

    for info in data.values():
        total += info["nilai"]

    return total / len(data)


# Data awal mahasiswa
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}


# 1. Mencari mahasiswa berdasarkan NIM
print("=" * 45)
print("       SISTEM DATA MAHASISWA")
print("=" * 45)

nim_cari = input("\nMasukkan NIM yang dicari: ").strip().upper()
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)

if hasil is not None:
    print("\nData mahasiswa ditemukan!")
    print(f"NIM   : {nim_cari}")
    print(f"Nama  : {hasil['nama']}")
    print(f"Kelas : {hasil['kelas']}")
    print(f"Nilai : {hasil['nilai']}")
else:
    print("Data tidak ditemukan.")


# 2. Menambahkan mahasiswa baru
print("\n--- Tambah Mahasiswa ---")

nim_baru = input("Masukkan NIM baru: ").strip().upper()

if not nim_baru:
    print("NIM tidak boleh kosong.")
elif nim_baru in data_mahasiswa:
    print("NIM sudah terdaftar.")
else:
    nama_baru = input("Masukkan nama: ").strip()
    kelas_baru = input("Masukkan kelas: ").strip().upper()

    try:
        nilai_baru = float(input("Masukkan nilai: "))

        if not nama_baru or not kelas_baru:
            print("Nama dan kelas tidak boleh kosong.")
        elif not 0 <= nilai_baru <= 100:
            print("Nilai harus antara 0 sampai 100.")
        else:
            data_mahasiswa[nim_baru] = {
                "nama": nama_baru,
                "kelas": kelas_baru,
                "nilai": nilai_baru
            }
            print("Mahasiswa berhasil ditambahkan.")

    except ValueError:
        print("Nilai harus berupa angka.")


# 3. Mengubah nilai mahasiswa
print("\n--- Ubah Nilai Mahasiswa ---")

nim_ubah = input("Masukkan NIM yang nilainya akan diubah: ").strip().upper()

if nim_ubah in data_mahasiswa:
    try:
        nilai_update = float(input("Masukkan nilai baru: "))

        if 0 <= nilai_update <= 100:
            data_mahasiswa[nim_ubah]["nilai"] = nilai_update
            print("Nilai berhasil diperbarui.")
        else:
            print("Nilai harus antara 0 sampai 100.")

    except ValueError:
        print("Nilai harus berupa angka.")
else:
    print("Data mahasiswa tidak ditemukan.")


# 4. Menampilkan seluruh data mahasiswa
print("\n" + "=" * 65)
print("                 REKAP DATA MAHASISWA")
print("=" * 65)

for nim, info in data_mahasiswa.items():
    print(
        f"NIM: {nim} | "
        f"Nama: {info['nama']} | "
        f"Kelas: {info['kelas']} | "
        f"Nilai: {info['nilai']:g}"
    )


# 5. Menghitung rata-rata nilai mahasiswa
print("-" * 65)

rata_rata = rata_rata_nilai(data_mahasiswa)

print(f"Jumlah mahasiswa : {len(data_mahasiswa)}")
print(f"Rata-rata nilai  : {rata_rata:.2f}")
print("=" * 65)
