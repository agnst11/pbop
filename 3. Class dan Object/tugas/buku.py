class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit


buku1 = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938)
buku2 = Buku('Laskar Pelangi', 'Andrea Hirata', 2005)
buku3 = Buku('Bukannya Aku Nggak Mau Menikah', 'Lee Joo Yoon', 2021)

perpus = [buku1, buku2, buku3]


for i in perpus:
    print(
        f'Buku {i.judul} karangan {i.pengarang} pertama kali diterbitkan tahun {i.tahun_terbit}')
