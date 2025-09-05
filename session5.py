from datetime import datetime
from random import random

tahunlahir = int(input("Masukkan Tanggal Lahir Anda"))
tahunsekarang = datetime.now().year

print (tahunsekarang - tahunlahir)

