# Polymorpism dengan class

class kucing:
    def __init__(self, nama, umur) -> None:
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print('meow')

class dog:
    def __init__(self, nama, umur) -> None:
        self.nama = nama
        self.umur = umur

    def bersuara(self):
        print('Guk.... Gukk... Guk....')


cat = kucing('Moly', '3 tahun')
anjing= dog('ethan', '3 tahun')

for hewan in (cat, anjing):
    hewan.bersuara()