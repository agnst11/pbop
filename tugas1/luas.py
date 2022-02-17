def showMenu():
    print('''
    1. Persegi
    2. Persegi Panjang
    3. Lingkaran
    4. Segitiga''')


def persegi():
    s = int(input('> Input Sisi : '))
    print('-> Luas Persegi :', s*s)


def persegiPanjang():
    p = int(input('> Input Panjang : '))
    l = int(input('> Input Lebar : '))
    print('-> Luas Persegi Panjang :', p*l)


def lingkaran():
    pi = 3.14
    r = int(input('> Input Jari - Jari : '))
    print('-> Luas Lingkaran :', pi*(r**2))


def segitiga():
    a = int(input('> Input Alas : '))
    t = int(input('> Input Tinggi : '))
    print('-> Luas Segitiga :', a*t/2)


while True:
    print('\n----- Hitung Luas -----')
    showMenu()
    menu = int(input('\n> Pilih Menu : '))

    if menu == 1:
        persegi()
    elif menu == 2:
        persegiPanjang()
    elif menu == 3:
        lingkaran()
    elif menu == 4:
        segitiga()
    else:
        break
