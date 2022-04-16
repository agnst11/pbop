import mysql.connector
import os
from colorama import Fore, Style
from datetime import datetime

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '',
    database = 'perpusNew'
)

cur = db.cursor()

class perpusNew:
    def addItem(self,id, judul, pengarang, status):
        self.id = id
        self.judul = judul
        self.pengarang = pengarang
        self.status = status

        cur.execute(f"INSERT INTO `buku`(`id`, `judul`, `pengarang`, `status`) VALUES ('{self.id}','{self.judul}','{self.pengarang}','{self.status}')")
        db.commit()
        print(Fore.GREEN + 'Data berhasil ditambahkan'+ Style.RESET_ALL)
    
    def showItem(self):
        cur.execute(f"SELECT * FROM `buku`;")
        data = cur.fetchall()
        for i in data:
            print(f'''> ID          : {i[0]}
> Judul       : {i[1]}
> Pengarang   : {i[2]}
> Status      : {i[3]} \n''')

    def searchItem(self, judul):
        self.judul = judul
        cur.execute(f"SELECT * FROM `buku` WHERE `judul` LIKE '%{self.judul}%'")
        data = cur.fetchall()
        if data != []:
            for i in data:
                print(f'''> ID          : {i[0]}
> Judul       : {i[1]}
> Pengarang   : {i[2]}
> Status      : {i[3]} \n''')

        else:
            print(Fore.RED + 'Data tidak ditemukan ' + Style.RESET_ALL)

    def delItem(self,id):
        self.id = id
        cur.execute(f"SELECT * FROM `buku` WHERE `id` = '{self.id}'")
        if cur.fetchall() != []:
            cur.execute(f"DELETE FROM `buku` WHERE `id` = '{self.id}' ")
            db.commit()
            print(Fore.GREEN + 'Data Berhasil Dihapus '+ Style.RESET_ALL)
        else:
            print(Fore.RED + 'Data tidak ditemukan ' + Style.RESET_ALL)


class user:
    def pinjam(self, idBuku, userId, username):
        self.idBuku = idBuku
        self.userId = userId
        self.username = username 

        cur.execute(f"SELECT `status` FROM `buku` WHERE `id`= '{self.idBuku}';")
        data = cur.fetchall()
        if data != []:
            if 'ada' == data[0][0]:
                cur.execute(f"UPDATE `buku` SET `status`='dipinjam' WHERE `id` = '{self.idBuku}'")
                cur.execute(f"INSERT INTO `pinjam`(`userid`, `username`, `idBuku`, `waktu`) VALUES ('{self.userId}','{self.username}','{self.idBuku}','{datetime.now()}')")
                db.commit()
                print(Fore.GREEN + 'Buku Berhasil Dipinjam ' + Style.RESET_ALL)

            else:
                print(Fore.RED + 'maaf buku tersebut sedang dipinjam' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'data buku tidak ditemukan' + Style.RESET_ALL)

    def kembali(self, userId, idBuku):
        self.userId = userId
        self.idBuku = idBuku

        cur.execute(f"SELECT * FROM `pinjam` WHERE `userid` = {self.userId} AND `idBuku` = {self.idBuku} ")
        if cur.fetchall() != []:
            cur.execute(f"UPDATE `buku` SET `status`='ada' WHERE `id` = '{self.idBuku}'")
            cur.execute(f"DELETE FROM `pinjam` WHERE `userid` = {self.userId} AND `idBuku` = {self.idBuku}")
            db.commit()
            print(Fore.GREEN + 'Buku Berhasil Dikembalikan ' + Style.RESET_ALL)
        else:
            print(Fore.RED + "data tidak ditemukan"+ Style.RESET_ALL)


p = perpusNew()
u = user()

while True:
    os.system('cls')
    print('''
    1. Insert Item
    2. Delete Item
    3. Show Item
    4. Search Item
    5. Pinjam
    6. Kembalikan
    7. Exit''')

    menu = input('-> Pilih Menu : ')
    if menu == '1':
        os.system('cls')
        idBuku = int(input('-> Masukan ID Buku : '))
        judul = input('-> Masukan Judul Buku : ')
        pengarang = input('-> Masukan Nama Pengarang : ')
        status = input('-> Masukan Status Buku (ada/dipinjam) : ')
        p.addItem(idBuku, judul, pengarang, status)
        input('\n.....')

    elif menu == '2':
        os.system('cls')
        idBuku = int(input('-> Masukan ID Buku : '))
        p.delItem(idBuku)
        input('\n.....')

    elif menu == '3':
        os.system('cls')
        print(Fore.BLUE +'-'*8, 'Data Buku', '-'*8 + Style.RESET_ALL)
        p.showItem()
        input('\n.....')

    elif menu == '4':
        os.system('cls')
        judul = input('-> Masukan Judul : ')
        print(Fore.BLUE +'-'*8, 'Data Buku', '-'*8 + Style.RESET_ALL)
        p.searchItem(judul)
        input('\n.....')

    elif menu == '5':
        os.system('cls')
        idBuku = int(input('-> Masukan ID Buku : '))
        userId = int(input('-> Masukan User ID : '))
        username = input('-> Masukan Username : ')
        u.pinjam(idBuku, userId, username)
        input('\n.....')
        

    elif menu == '6':
        os.system('cls')
        userId = int(input('-> Masukan User ID : '))
        idBuku = int(input('-> Masukan ID Buku : '))
        u.kembali(userId,idBuku)
        input('\n.....')

    elif menu == '7':
        exit()
    else:
        print(Fore.RED + 'Maaf Pilihan Menu Tidak Tersedia' + Style.RESET_ALL)