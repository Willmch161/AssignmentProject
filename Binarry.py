# Nilai desimal
a = 12
b = 9

# Operasi bitwise
hasil_and = a & b  # AND
hasil_or = a | b   # OR

# Menampilkan hasil dalam desimal dan biner
print(f"a = {a}, b = {b}")
print(f"a dalam biner: {bin(a)[2:]}")  # Mengubah ke biner tanpa '0b'
print(f"b dalam biner: {bin(b)[2:]}")

print(f"a & b = {hasil_and} (Biner: {bin(hasil_and)[2:]})")  # AND
print(f"a | b = {hasil_or} (Biner: {bin(hasil_or)[2:]})")    # OR
