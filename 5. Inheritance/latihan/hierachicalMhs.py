class mahasiswa:
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

class siswa1(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

    def detSiswa1(self):
        print(self.nama, 'alamat : Wall Rose')

class siswa2(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

    def detSiswa2(self):
        print(self.nama, 'jurusan : Informatika')

m1 = siswa1('esa', 124535)
m2 = siswa2('bella',124224)

print(m1.nim)
m1.detSiswa1()

print(m2.nama)
m2.detSiswa2()