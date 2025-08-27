def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Pembagian dengan nol"
    return x / y

def main():
    print("Kalkulator Sederhana")
    print("Pilih Operasi:")
    print("1. +")
    print("2. -")
    print("3. ×")
    print("4. ÷")

    choice = input("Masukan Pilihan (1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("Kesalahan input")
        return

    try:
        num1 = float(input("Masukan angka pertama: "))
        num2 = float(input("Masukan angka kedua: "))
    except ValueError:
        print("Kesalahan: Masukan harus berupa angka.")
        return

    if choice == '1':
        print("Hasil:", add(num1, num2))
    elif choice == '2':
        print("Hasil:", subtract(num1, num2))
    elif choice == '3':
        print("Hasil:", multiply(num1, num2))
    elif choice == '4':
        print("Hasil:", divide(num1, num2))

if __name__ == "__main__":
    main()