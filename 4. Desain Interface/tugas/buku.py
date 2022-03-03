class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, penerbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__penerbit = penerbit


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938, 'erlangga')
buku2 = Buku('Laskar Pelangi', 'Andrea Hirata', 2005, 'erlangga')
buku3 = Buku('Bukannya Aku Nggak Mau Menikah',
             'Lee Joo Yoon', 2021, 'erlangga')

perpus = [buku1, buku2, buku3]

for i in perpus:
    print(
        f'Buku {i.judul} karangan {i.pengarang} pertama kali diterbitkan tahun {i.tahun_terbit} oleh {i._Buku__penerbit}')
