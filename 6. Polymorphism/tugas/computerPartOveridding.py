# parent
class computerPart:
    def __init__(self,pabrikan, nama, jenis, harga):
        self.pabrikan = pabrikan
        self.nama = nama
        self.jenis = jenis
        self.harga = harga

    def show(self):
        print(f'{self.nama} harga {self.harga}')

class processor(computerPart):
    def __init__(self,pabrikan,nama,harga,jumlahCore, speed):
        super().__init__(pabrikan, nama, "Processor", harga)
        self.jumlahCore = jumlahCore
        self.speed = speed
    def show(self):
        print(f'{self.nama} merupakan bagian dari komputer')

class ram(computerPart):
    def __init__(self,pabrikan, nama, harga, kapasitas):
        super().__init__(pabrikan,nama,"RAM",harga)
        self.kapasitas = kapasitas

class hardDisk(computerPart):
    def __init__(self, pabrikan, nama, harga,  kapasitas, rpm):
        super().__init__(pabrikan, nama, "Sata", harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

c = computerPart('Asus','ROG Tower','Gaming', '10000000')
p = processor('Intel', 'Core i5 8520', 2500000, 8, '3.5GHz')

c.show()
p.show()