class Pegawai:
    __nama = ''
    __alamat = ''
    __gaji = 0

    def __init__(self, nama, alamat) -> None:
        self.__nama = nama
        self.__alamat = alamat

    def __hitungGaji(self):
        upahLembur = 20000
        gajiPokok = 2000000
        jumLembur = int(input('Jumlah Lembur : '))
        self.__gaji = (upahLembur*jumLembur) + gajiPokok

    def tampilDetail(self):
        print('Menghitung dan menampilkan Detail gaji pegawai')
        self.__hitungGaji()
        print(f'''
        Nama: {self.__nama}
        Alamat: {self.__alamat}
        Gaji: {self.__gaji}''')


pgw1 = Pegawai('Mikasa Ackerman', 'Nganjuk')
pgw1.tampilDetail()

pgw2 = Pegawai('Killua', 'Greed Island')
pgw2.tampilDetail()
