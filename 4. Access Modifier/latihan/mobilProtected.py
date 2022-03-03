class Mobil:
    def __init__(self, jendela, pintu, mesin) -> None:
        self._jendela = jendela
        self._pintu = pintu
        self._mesin = mesin


class truk(Mobil):
    def __init__(self, jendela, pintu, mesin, Merk) -> None:
        super().__init__(jendela, pintu, mesin)
        self._merk = Merk


tes = truk(2, 2, 'diesel', 'yamaha')

# memanggil protected
print(
    f'Truk dengan {tes._pintu} Pintu dan {tes._jendela} Jendela ini bermesin {tes._mesin} dibuat oleh {tes._merk}')
