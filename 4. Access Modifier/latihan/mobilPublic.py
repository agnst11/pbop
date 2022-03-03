class Mobil:
    def __init__(self, jendela, pintu, mesin) -> None:
        self.jendela = jendela
        self.pintu = pintu
        self.mesin = mesin


class sedan(Mobil):
    def __init__(self, jendela, pintu, mesin, Merk) -> None:
        super().__init__(jendela, pintu, mesin)
        self.merk = Merk


tes = sedan(2, 2, '500 HP', 'Audi')

# memanggil protected
print(
    f'Sedan dengan {tes.pintu} Pintu dan {tes.jendela} Jendela ini bermesin {tes.mesin} dibuat oleh {tes.merk}')
