class Titik:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Garis:
    def __init__(self, titikPertama, titikKedua):
        self.titikPertama = titikPertama
        self.titikKedua = titikKedua

    def panjang(self):
        pjgX = self.titikKedua.x - self.titikPertama.x
        pjgY = self.titikKedua.y - self.titikPertama.y
        pjg = (pjgX**2 + pjgY**2) ** 0.5
        return pjg


titik_a = Titik(0, 0)
titik_b = Titik(3, 4)

garis_ab = Garis(titik_a, titik_b)
print('Panjang garis ab adalah ', garis_ab.panjang())
