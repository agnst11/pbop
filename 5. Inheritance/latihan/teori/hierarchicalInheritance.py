# parent
class induk:
    def fungsiInduk(self):
        print('fungsi induk')

# child class 1
class anak1(induk):
    def fungsiAnak1(self):
        print('fungsi anak pertama')


# child class 2
class anak2(induk):
    def fungsiAnak2(self):
        print('fungsi anak kedua')

a1 = anak1()
a2 = anak2()

a1.fungsiAnak1()
a1.fungsiInduk()

a2.fungsiAnak2()
a2.fungsiInduk()