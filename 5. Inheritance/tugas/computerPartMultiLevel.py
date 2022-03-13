class computerPart:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

# class processor(computerPart):
#     def __init__(self,pabrikan,nama,harga,jumlahCore, speed):
#         super().__init__(pabrikan, nama, "Processor", harga)
#         self.jumlahCore = jumlahCore
#         self.speed = speed


# class ram(computerPart):
#     def __init__(self,pabrikan, nama, harga, kapasitas):
#         super().__init__(pabrikan,nama,"RAM",harga)
#         self.kapasitas = kapasitas

class storage(computerPart):
    def __init__(self, nama, harga, jenis):
        super().__init__(nama, harga)
        self.jenis = jenis


class hdd(storage):
    def __init__(self,nama, harga, kapasistas):
        super().__init__(nama, harga, 'HDD')
        self.kapasitas = kapasistas


pc = hdd('Toshiba',500000,'1 TB')


print(pc.jenis)