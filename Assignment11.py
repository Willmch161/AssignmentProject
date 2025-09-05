nilai_siswa = {
    "A001": 85,
    "A002": 90,
    "A003": 78
}

def tampil_data():
    print("\n=== Daftar Nilai Siswa ===")
    for nim, nilai in nilai_siswa.items():
        print(f"{nim}: {nilai}")

def tambah_atau_ubah():
    nim = input("Masukkan NIM: ")
    try:
        nilai = int(input("Masukkan Nilai: "))
        nilai_siswa[nim] = nilai
        print("Data disimpan.")
    except ValueError:
        print("Nilai harus berupa angka.")

def lihat_nilai():
    nim = input("Masukkan NIM yang ingin dilihat: ")
    print("Nilai:", nilai_siswa.get(nim, "Tidak ditemukan."))

def hapus_data():
    nim = input("Masukkan NIM yang akan dihapus: ")
    if nim in nilai_siswa:
        del nilai_siswa[nim]
        print("Data dihapus.")
    else:
        print("Data tidak ada.")

def jumlah_data():
    print("Jumlah data:", len(nilai_siswa))

def menu():
    print("\n1. Tampil")
    print("2. Tambah/Ubah")
    print("3. Lihat")
    print("4. Hapus")
    print("5. Jumlah")
    print("6. Keluar")

def main():
    while True:
        menu()
        p = input("Pilih: ")
        if p == "1":
            tampil_data()
        elif p == "2":
            tambah_atau_ubah()
        elif p == "3":
            lihat_nilai()
        elif p == "4":
            hapus_data()
        elif p == "5":
            jumlah_data()
        elif p == "6":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan salah.")

main()