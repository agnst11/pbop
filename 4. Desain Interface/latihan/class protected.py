class Utama:
    def __init__(self) -> None:
        self._a = 2


class Turunan:
    def __init__(self) -> None:
        Utama.__init__(self)
        print('Memanggil variable protected ', self._a)

        # ubah variable protected
        self._a = 3
        print(self._a)


objek1 = Turunan()
objek2 = Utama()

print('panggil variable protected dari objek1', objek1._a)
print('panggil variable protected dari objek2 ', objek2._a)
