import mysql.connector
from colorama import Fore, Style
from datetime import  datetime

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='sewa'
)
cur = db.cursor()


class admin:
    def __init__(self, nama, password) -> None:
        self.__nama = nama
        self.__password = password

    def __cekAdmin(self):
        if self.__nama == 'danu' and self.__password == '1234':
            return True

class sepeda:
    time = datetime.now()
    def addItem(self, id, warna, harga, status):
        self.id = id
        self.warna = warna
        self.harga = harga
        self.status = status
        cur.execute(f"INSERT INTO `sepeda`(`id`, `warna`, `harga`, `status`) VALUES ('{self.id}','{self.warna}','{self.harga}','{self.status}')")
        db.commit()
        print(Fore.GREEN + '> Data berhasil ditambahkan' + Style.RESET_ALL)
        
    def delItem(self, id):
        self.id = id
        cur.execute(f"SELECT * FROM `sepeda` WHERE `id` = '{self.id}';")
        if cur.fetchall() != []:
            cur.execute(f"DELETE FROM `sepeda` WHERE `id` = '{self.id}';")
            db.commit()
            print(Fore.GREEN + '> Data berhasil dihapus' + Style.RESET_ALL)

        else:
            print(Fore.RED+'> Data tidak ditemukan'+Style.RESET_ALL)
        

    def showItem():
        cur.execute('SELECT * FROM `sepeda`')
        data = cur.fetchall()
        x = 1
        print('~'*22,'LIST SEPEDA','~'*22)
        print('>\tID \t| Warna \t| Harga Sewa \t| Status \n')
        for i in data:
            print(f'> {x}. {i[0]} \t| {i[1]}  \t| {i[2]}  \t| {i[3]} ')
            x += 1
        return data
        # print(data)

    def updateItem(self, id, harga, ubah):
        self.id = id
        self.harga = harga
        self.ubah = ubah
        try:
            cur.execute(f"UPDATE `sepeda` SET `{self.ubah}`='{self.harga}' WHERE `id` = '{self.id}'")
            db.commit()
            print(Fore.GREEN+'> Data berhasil diupdate'+Style.RESET_ALL)
        except:
            print(Fore.RED+'> Terjadi error saat proses update data'+ Style.RESET_ALL)

    def searchItem(self, id):
        self.id = id 
        cur.execute(f"SELECT * FROM `sepeda` WHERE `id` = '{self.id}';")
        data = cur.fetchall()
        return data

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


    def cetakStruk(self):
        time = datetime.now()
        with open('Sewa-'+self.nik+'-'+self.idSepeda+'.txt', 'w+') as f:
            f.write(f'''
    Nama Penyewa: {self.nama}
    NIK Penyewa : {self.nik}
    No Hp.      : {self.noHp}
    ID Sepeda   : {self.idSepeda}
    Sewa/jam    : {self.harga}
    Durasi Sewa : {self.durasi} 
    Waktu Sewa  : {time}\n\n''')
            f.close()

        cur.execute(f"UPDATE `sepeda` SET `status`='disewa' WHERE `id` = '{self.idSepeda}'")
        cur.execute(f"INSERT INTO `data_sewa`(`nama`, `nik`, `noHp`, `idSepeda`, `harga`, `durasi`, `waktuSewa`) VALUES ('{self.nama}','{self.nik}','{self.noHp}','{self.idSepeda}','{self.harga}','{self.durasi}','{time}')")
        db.commit()
    
    def pembayaran(self, harga, durasi, waktuSewa):
        x = datetime.now()
        self.time = f"{x.year}-{x.month}-{x.day} {x.hour}:{x.minute}:{x.second}"
        self.harga = harga
        self.durasi = durasi
        self.waktuSewa = waktuSewa

        cekDenda = datetime.strptime(f'{self.time}','%Y-%m-%d %H:%M:%S') - datetime.strptime(f'{self.waktuSewa}', '%Y-%m-%d %H:%M:%S')

        if int(cekDenda.seconds/60) <= self.durasi * 60 + 10:
            self.denda = 0

        elif int(cekDenda.seconds/60) <= self.durasi * 60 + 120 :
            telat = (int(cekDenda.seconds/60)- int(self.durasi*60+10)) / 10
            self.denda = round(telat * 2000)
        
        else: 
           self.denda = 50000

        self.tagihan = self.harga * self.durasi + self.denda
        print('\n> Biaya Sewa Sepeda          :', self.harga*self.durasi)
        print('> Biaya Denda Keterlambatan  :', self.denda)
        print('> Tagihan yang harus dibayar :', self.tagihan)
        
        self.bayar = int(input('\n-> Masukan Nominal Pembayaran : '))
        while self.bayar < self.tagihan:
            print(Fore.RED+'> Nominal yang anda bayarkan tidak sesuai'+Style.RESET_ALL)
            self.bayar = int(input('\n-> Masukan Nominal Pembayaran : '))

        self.kembalian = self.bayar - self.tagihan


    def kembalikan(self,nik,nama,idSepeda):
        self.nik = nik
        self.nama = nama
        self.idSepeda = idSepeda
        with open('Sewa-'+self.nik+'-'+self.idSepeda+'.txt', 'a') as f:
            # f.writelines()
            f.writelines(f'''
        {'~'*15} Pengembalian Sepeda {'~'*15}
        Waktu Kembali       : {self.time}
        Biaya Sewa Sepeda   : {self.harga*self.durasi}
        Denda Keterlambatan : {self.denda}
        Total Tagihan       : {self.tagihan}\n
        Uang yang dibayarkan: {self.bayar}
        Kembalian           : {self.kembalian}\n
        {'~'*18} Terima Kasih  {'~'*18}
        
         ''')
            f.close()

        cur.execute(f"UPDATE `sepeda` SET `status`='tersedia' WHERE `id` = '{self.idSepeda}'")
        cur.execute(f"UPDATE `data_sewa` SET `waktuKembali`='{self.time}',`tagihan`='{self.tagihan}' WHERE `nik` = '{self.nik}' AND `idSepeda` = '{self.idSepeda}'")
        db.commit()


    def cariDataSewa(self, nik, idSepeda):
        self.nik = nik
        self.idSepeda = idSepeda

        cur.execute(f"SELECT `nik`, `nama`, `noHp`, `idSepeda`, `harga`, `durasi`, `waktuSewa` FROM `data_sewa` WHERE `nik` = '{self.nik}' AND `idSepeda` = '{self.idSepeda}';")
        data = cur.fetchall()
        return data






