class mahasiswa:
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

    def detMhs(self):
        return self.nama, self.nim

    def cekMhs(self):
        if self.nim < 150000:
            return 'Mahasiswa Aktif'
        else:
            return 'Mahasiswa tidak terdaftar'

class siswa(mahasiswa):
    def end(self):
        print('Mahasiswa belum melakukan daftar ulang')



m1 = mahasiswa('Danu', 140303)
print(m1.detMhs(), m1.cekMhs())

m2 = siswa('esa', 155000)
print(m2.detMhs(), m2.cekMhs())
m2.end()