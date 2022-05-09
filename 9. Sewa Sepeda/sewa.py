import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sewa'
)


class admin:
    def __init__(self, nama, password) -> None:
        self.nama = nama
        self.password = password

    def __cekAdmin(self):
        if self.nama == 'danu' and self.password == '1234':
            return True

class sepeda:
    
    def addItem(self, id, warna, status):
        pass

    def delItem(self, id):
        self.id = id

    def showItem():
        pass

    def updateItem(self, id):
        self.id = id

class penyewa:
    def __init__(self, nama, nik, noHp) -> None:
        self.nama = nama
        self.nik = nik
        self. noHp = noHp

class sewa(penyewa):
    def __init__(self, nama, nik, noHp, idSepeda, harga, Durasi):
        super().__init__(nama, nik, noHp)
        self. idSepeda = idSepeda
        self.harga = harga
        self.durasi = Durasi

    def kembalikan(self, nik, idSepeda):






while True:
    nama = input('masukan nama : ')
    password = input('masukan password : ')
    user = admin(nama, password)

    if user._admin__cekAdmin() == True:
        print('Selamat Datang')

    else:
        print('anda bukan admin')