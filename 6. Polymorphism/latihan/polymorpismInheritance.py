# Polymorpism dengan Inheritance 
class Burung: 
    def intro(self):
        print('Di Dunia ini ada beberapa type berbeda dari spesies burung')

    def terbang(self):
        print('hampir semua burung dapat terbang, namun ada beberapa yang tidak  dapat terbang')

class elang(Burung):
    def terbang(self):
        print('Elang dapat terbang')


class burungUnta(Burung):
    def terbang(self):
        print('burung unta tidak dapat terbang')

objBurung = Burung()
objElang = elang()
objUnta = burungUnta()

objBurung.intro()
objBurung.terbang()

objElang.intro()
objElang.terbang()

objUnta.intro()
objUnta.terbang()