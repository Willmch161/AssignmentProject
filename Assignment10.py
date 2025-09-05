nilai_siswa = {"A001": 85, "A002": 90, "A003": 78}

while True:
    print("\n1.Tampil 2.Tambah/Ubah 3.Lihat 4.Hapus 5.Jumlah 6.Keluar")
    p = input("Pilih: ")

    if p == "1":
        for nim, nilai in nilai_siswa.items():
            print(f"{nim}: {nilai}")
            
    elif p == "2":
        nim = input("NIM: ")
        nilai = int(input("Nilai: "))
        nilai_siswa[nim] = nilai
        print("Data disimpan.")

    elif p == "3":
        nim = input("NIM: ")
        print("Nilai:", nilai_siswa.get(nim, "Tidak ditemukan."))

    elif p == "4":
        nim = input("NIM yang dihapus: ")
        if nim in nilai_siswa:
            del nilai_siswa[nim]
            print("Data dihapus.")
        else:
            print("Data tidak ada.")

    elif p == "5":
        print("Jumlah data:", len(nilai_siswa))

    elif p == "6":
        break

    else:
        print("Pilihan salah.")
