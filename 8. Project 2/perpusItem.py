import mysql.connector
from colorama import Fore, Style

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'perpusitem')

cur = db.cursor()

class perpusItem:
    def __init__(self, judul, subjek, lokasi, status) -> None:
        self.judul = judul
        self.subjek = subjek
        self.lokasi = lokasi
        self.status = status


class buku(perpusItem):
    def __init__(self, judul, lokasi, isbn, namaPengarang, jmlHal, ukuran ,status) -> None:
        super().__init__(judul, 'buku', lokasi, status)
        self.isbn = isbn
        self.namaPengarang = namaPengarang
        self.jmlHal = jmlHal
        self.ukuran = ukuran

        cur.execute(f"INSERT INTO {self.subjek} (judul, lokasi, isbn, pengarang, jmlHal, ukuran, status) VALUES ( '{self.judul}', '{self.lokasi}', {self.isbn}, '{self.namaPengarang}', {self.jmlHal}, '{self.ukuran}', '{self.status}' ) ")
        db.commit()

class majalah(perpusItem):
    def __init__(self, judul, lokasi, volume, issue, status) -> None:
        super().__init__(judul, 'majalah', lokasi, status)
        self.volume = volume
        self.issue = issue

        cur.execute(f"INSERT INTO {self.subjek} (judul, lokasi, volume, issue, status) VALUES ( '{self.judul}', '{self.lokasi}',  '{self.volume}', '{self.issue}', '{self.status}' ) ")
        db.commit()

class dvd(perpusItem):
    def __init__(self, judul, lokasi, aktor, genre, status) -> None:
        super().__init__(judul, 'dvd', lokasi, status)
        self.aktor = aktor
        self.genre = genre

        cur.execute(f"INSERT INTO {self.subjek} (judul, lokasi, aktor, genre, status) VALUES ('{self.judul}', '{self.lokasi}',  '{self.aktor}', '{self.genre}', '{self.status}')")
        db.commit()

class katalog:
    def cari(self, judul, subjek):
        self.judul = judul
        self.subjek = subjek

        cur.execute(f"SELECT * FROM {self.subjek} WHERE {self.subjek}.judul LIKE '%{self.judul}%';")
        data = cur.fetchall()

        print(f'\nDaftar {self.subjek}')
        if data != []:
            for i in data:
                print(i)
        else:
            print(Fore.RED + f'Data {self.subjek} tidak ditemukan ' + Style.RESET_ALL)

class pengarang:
    def cari(self, nama):
        self.nama = nama
        cur.execute(f"SELECT buku.judul,buku.pengarang FROM buku WHERE buku.pengarang LIKE '%{self.nama}%'")
        data = cur.fetchall()
        if data != []:
            for i in data:
                print(i)
        else:
            print(Fore.RED + f'Pengarang dengan nama {self.nama} tidak ditemukan ' + Style.RESET_ALL)


while True:
    print('''
    1. Insert Data
    2. Katalog
    3. Pengarang''')
    menu = input('pilih menu : ')
    if menu == '1':
        print('''
        1. Data Buku
        2. Data Majalah
        3. Data DvD''')
        pilih = input('Pilih Data : ')

        if pilih == '1':
            judul = input('Masukan Judul Buku : ')
            lokasi = input('Masukan Tempat Menaruh Buku : ')
            isbn = int(input('Masukan ISBN : '))
            namaPengarang = input('Masukan Nama Pengarang : ')
            jmlHal = int(input('Masukan Jumlah Halaman : '))
            ukuran = input('Masukan Ukuran Buku : ')
            status = input('Status Buku (ada/dipinjam) : ')
            
            buku(judul,lokasi,isbn, namaPengarang, jmlHal, ukuran,status)

            print(Fore.GREEN + 'Data Berhasil Ditambahkan' + Style.RESET_ALL)
            input("")
        
        elif pilih == '2':
            judul = input('Masukan Judul Majalah : ')
            lokasi = input('Masukan Tempat Menaruh Majalah : ')
            volume = input('Masukan Volume : ')
            issue = input('Masukan Issue : ')
            status = input('Status Majalah (ada/dipinjam) : ')
            
            majalah(judul,lokasi, volume, issue,status)

            print(Fore.GREEN + 'Data Berhasil Ditambahkan' + Style.RESET_ALL)
            input("")
        
        elif pilih == '3':
            judul = input('Masukan Judul dvd : ')
            lokasi = input('Masukan Tempat Menaruh dvd : ')
            aktor = input('Masukan aktor : ')
            genre = input('Masukan genre : ')
            status = input('Status dvd (ada/dipinjam) : ')
            
            dvd(judul,lokasi, aktor, genre,status)

            print(Fore.GREEN + 'Data Berhasil Ditambahkan' + Style.RESET_ALL)
            input("")

        else: 
            print('Maaf Pilihan Kamu tidak tersedia')

    elif menu == '2':
        data = ['buku', 'majalah', 'dvd']
        judul = input('Masukan Judul : ')
        s = katalog()
        for i in data:
            s.cari(judul,i)
        input("")
    
    elif menu == '3':
        p = pengarang()

        nama = input('Masukan Nama Pengarang : ')
        p.cari(nama)
