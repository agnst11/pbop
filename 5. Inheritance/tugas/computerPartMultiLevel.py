class computerPart:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class storage(computerPart):
    def __init__(self, nama, harga, jenis):
        super().__init__(nama, harga)
        self.jenis = jenis


class hdd(storage):
    def __init__(self,nama, harga, kapasistas):
        super().__init__(nama, harga, 'HDD')
        self.kapasitas = kapasistas


pc = hdd('Toshiba',500000,'1 TB')

print(f'Computer dengan penyimpanan jenis {pc.jenis} yang berkapasitas {pc.kapasitas}')