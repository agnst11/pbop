class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def tampilMhs(self):
        print(f'\n\nnama : {self.nama}, nim {self.nim}')

    def hitungSks(self, jmlsks=None, sks=None):
        if jmlsks != None and sks !=None :
            totalSks = jmlsks + sks
            print('total sks =', totalSks)

        else:
            totalSks=jmlsks
            print('Total sks =',totalSks)


class dpa(Mahasiswa):
    def __init__(self, nama, nim):
        super().__init__(nama, nim)

    def tampilMhs(self):
        print(f'''
        Detail Mahasiswa
        Nama    : {self.nama}
        Nim     : {self.nim}''')

m1 = Mahasiswa('Luffy', 231412)
d = dpa('eren', 123442)

d.tampilMhs()
m1.tampilMhs()