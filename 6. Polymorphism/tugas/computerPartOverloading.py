# parent
class computerPart:
    def __init__(self,pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

class processor(computerPart):
    def __init__(self,pabrikan,nama,harga,jumlahCore, speed):
        super().__init__(pabrikan, nama, "Processor", harga)
        self.jumlahCore = jumlahCore
        self.speed = speed

    def totalHarga(self, jumlah):
        total = self.harga * jumlah
        print('Total harga :', total)

class ram(computerPart):
    def __init__(self,pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas

class hardDisk(computerPart):
    def __init__(self, pabrikan, nama, harga,  kapasitas, rpm):
        super().__init__(pabrikan, nama, "Sata", harga)
        self.kapasitas = kapasitas
        self.rpm = rpm


p = processor('Intel', 'Core i5 8520', 2500000, 8, '3.5GHz')
r = ram('V-Gen', 'DDR4 SODimm 2400Mhz', 380000, '8GB')
h = hardDisk('Seagate', 'HDD 2,5 Inch', 290000, '500GB',7200)

parts = [p,r,h]
for part in parts:
    print(f'{part.jenis} {part.nama} Produksi {part.pabrikan}')

p.totalHarga(2)