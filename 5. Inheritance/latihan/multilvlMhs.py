class mahasiswa:
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

class siswa1(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

class siswa2(mahasiswa):
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim


m1 = mahasiswa('Danu', 140303)
m2 = siswa1('esa', 124535)
m3 = siswa2('bella',124224)

print(m1.nama , m1.nim)
print(m2.nama)
print(m3.nim)