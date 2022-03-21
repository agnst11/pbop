# Implementasi Overloading
class Pegawai:
    jumlah = 0
    def __init__(self, nama, gaji) -> None:
        self.nama = nama
        self.gaji = gaji
        Pegawai.jumlah += 1

    def tampilPegawai(self):
        print(f'Nama : {self.nama}, gaji : {self.gaji}')

    #  Method Overloading
    def tunjangan(self, istri=None, anak=None):
        if anak != None and istri != None:
            total = anak + istri 
            print('Tunjangan anak + istri : ', total)
        
        else: 
            total = istri 
            print('tunjangan istri : ', total)

# memanggil class
peg1 = Pegawai('Eren', 2000)
peg2 = Pegawai('Luffy', 3000)

peg1.tampilPegawai()
peg2.tampilPegawai()

peg1.tunjangan(2500,2500)
peg2.tunjangan(2500)

print('total pegawai ',Pegawai.jumlah)
rata = (peg1.gaji + peg2.gaji)/ Pegawai.jumlah
print('Rata - rata gaji = ', rata)