print("== CALCULATOR APP ==")

while True:
    operator = input("Masukkan operator (+, -, *, /) atau 'quit' untuk keluar: ")

    if operator.lower() == "quit":
        print("Kalkulator ditutup. Terima kasih!")
        break

    if operator not in ['+', '-', '*', '/']:
        print("Operator tidak valid! Gunakan +, -, *, atau /.")
        continue

    while True:  # Loop untuk memastikan input angka yang valid
        try:
            num1 = float(input("Masukkan angka pertama: "))
            num2 = float(input("Masukkan angka kedua: "))
            break  # Keluar dari loop jika input benar
        except ValueError:
            print("Masukkan angka yang valid!")

    if operator == "+":
        hasil = num1 + num2
    elif operator == "-":
        hasil = num1 - num2
    elif operator == "*":
        hasil = num1 * num2
    elif operator == "/":
        while num2 == 0:  # Loop untuk menghindari pembagian dengan nol
            print("Error: Tidak bisa membagi dengan nol!")
            try:
                num2 = float(input("Masukkan angka kedua yang valid: "))
            except ValueError:
                continue
        hasil = num1 / num2

    print(f"Hasil: {hasil}\n")
