class Mahasiswa:
    def __init__(self, nama, nim, prodi, thn_masuk):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.thn_masuk = thn_masuk


m1 = Mahasiswa('Udin', '10120371', 'Sistem Informasi', 2020)
print(f'{m1.nama} adalah mahasiswa {m1.prodi} angkatan {m1.thn_masuk} dengan nim {m1.nim}')
