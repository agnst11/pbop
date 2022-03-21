# implementasi overloading
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        # self.prodi = prodi
        # self.thn_masuk = thn_masuk

    def tampilMhs(self):
        print(f'nama : {self.nama}, nim {self.nim}')

    def hitungSks(self, jmlsks=None, sks=None):
        if jmlsks != None and sks !=None :
            totalSks = jmlsks + sks
            print('total sks =', totalSks)

        else:
            totalSks=jmlsks
            print('Total sks =',totalSks)


m1 = Mahasiswa('eren', 123442)
m2 = Mahasiswa('Luffy', 231412)

m1.tampilMhs()
m2.tampilMhs()

m1.hitungSks(80, 34)
m2.hitungSks(83)