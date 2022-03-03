class Buku:
    def __init__(self, judul, pengarang, tahun_terbit, penerbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.__penerbit = penerbit


buku = Buku('Tenggelamnya Kapal Van Der Wijck', 'Hamka', 1938, 'Erlangga')
print(f'Buku {buku.judul} karangan {buku.pengarang} pertama kali diterbitkan tahun {buku.tahun_terbit}, diterbitkan oleh {buku._Buku__penerbit}')
