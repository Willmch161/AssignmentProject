def count_chars(text):
    return len (text)

def main():
    user_input = input ("Masukkan Kata Apa Saja: ")
    print (f"jumlah dalam karakter tersebut adalah: {count_chars(user_input)}")
    
if __name__ == "__main__":
    main()
