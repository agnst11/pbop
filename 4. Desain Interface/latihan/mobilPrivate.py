class Mobil:
    def __init__(self, jendela, pintu, mesin) -> None:
        self.__jendela = jendela
        self.__pintu = pintu
        self.__mesin = mesin


class Sport(Mobil):
    def __init__(self, jendela, pintu, mesin, warna) -> None:
        super().__init__(jendela, pintu, mesin)
        self.__warna = warna


tes = Sport(2, 2, '1300 HP', 'Merah')


# memanggil private
print(tes._Mobil__warna)
