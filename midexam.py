students = []

def insert_data():
    name = input("Masukkan nama mahasiswa: ")
    nim = input("Masukkan NIM mahasiswa: ")
    students.append({"name": name, "nim": nim})
    print(" Data berhasil ditambahkan.\n")

def show_data():
    if len(students) == 0:
        print("  Tidak ada data mahasiswa yang tersedia.\n")
    else:
        print(" Daftar Mahasiswa:")
        for i, student in enumerate(students):
            print(f"{i+1}. Nama: {student['name']}, NIM: {student['nim']}")
        print()

def edit_data():
    if len(students) == 0:
        print("  Tidak ada data untuk diedit.\n")
        return
    show_data()
    try:
        index = int(input("Masukkan nomor data yang ingin diedit: ")) - 1
        if 0 <= index < len(students):
            name = input("Masukkan nama baru: ")
            nim = input("Masukkan NIM baru: ")
            students[index] = {"name": name, "nim": nim}
            print(" Data berhasil diperbarui.\n")
        else:
            print(" Nomor tidak valid.\n")
    except ValueError:
        print(" Masukan harus berupa angka.\n")

def delete_data():
    if len(students) == 0:
        print("  Tidak ada data untuk dihapus.\n")
        return
    show_data()
    try:
        index = int(input("Masukkan nomor data yang ingin dihapus: ")) - 1
        if 0 <= index < len(students):
            deleted = students.pop(index)
            print(f" Data '{deleted['name']}' berhasil dihapus.\n")
        else:
            print(" Nomor tidak valid.\n")
    except ValueError:
        print(" Masukan harus berupa angka.\n")

def search_data():
    if len(students) == 0:
        print("  Tidak ada data untuk dicari.\n")
        return
    keyword = input("Masukkan nama atau NIM untuk dicari: ").lower()
    results = [s for s in students if keyword in s['name'].lower() or keyword in s['nim']]
    if results:
        print(" Hasil Pencarian:")
        for i, student in enumerate(results):
            print(f"{i+1}. Nama: {student['name']}, NIM: {student['nim']}")
        print()
    else:
        print(" Data tidak ditemukan.\n")

def exit_app():
    confirm = input(" Apakah kamu yakin ingin keluar? (y/n): ").lower()
    if confirm == 'y':
        print(" Aplikasi ditutup. Terima kasih.")
        return True
    else:
        print(" Kembali ke menu.\n")
        return False

# === PROGRAM UTAMA ===
while True:
    print("=== MENU DATA MAHASISWA ===")
    print("1. Insert Data")
    print("2. Show Data")
    print("3. Edit Data")
    print("4. Delete Data")
    print("5. Search Data")
    print("6. Exit")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
        insert_data()
    elif pilihan == "2":
        show_data()
    elif pilihan == "3":
        edit_data()
    elif pilihan == "4":
        delete_data()
    elif pilihan == "5":
        search_data()
    elif pilihan == "6":
        if exit_app():
            break
    else:
        print(" Pilihan tidak valid. Masukkan angka 1-6.\n")
1