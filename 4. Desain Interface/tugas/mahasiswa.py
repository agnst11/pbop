class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk, gender):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk
        self.__gender = gender


m1 = Mahasiswa('Udin', '10120371', 'Sistem Informasi', 2020, 'Laki - Laki')
m2 = Mahasiswa('Danu', '5210411165', 'Informatika', 2021, 'Laki - Laki')
m3 = Mahasiswa('Esa', '5210411159', 'Informatika', 2021, 'Laki - Laki')

data = [m1, m2, m3]

for i in data:
    print(f'{i.nama} adalah mahasiswa {i.prodi} angkatan {i.thn_masuk} dengan nim {i.nim} ia berjenis kelamin {i._Mahasiswa__gender}')
