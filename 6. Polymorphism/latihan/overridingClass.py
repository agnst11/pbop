# Overriding
class segiempat:
    def __init__(self, panjang, lebar) -> None:
        self.panjang = panjang
        self.lebar = lebar

    def luas(self):
        print('Luas Segiempat =', self.panjang * self.lebar, 'm^2')

class bujursangkar(segiempat):
    def __init__(self, sisi) -> None:
        self.side = sisi
        segiempat.__init__(self, sisi, sisi)

    def luas(self):
        print('Luas bujursangkar = ', self.side * self.side, 'm^2')

b = bujursangkar(4)
s = segiempat(2,4)

b.luas()
s.luas()