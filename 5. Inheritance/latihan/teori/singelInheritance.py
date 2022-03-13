# Class Parent 
class hewan:
    def bersuara(self):
        print("Kucin Bersuara ")


# child class dari hewan
class kucing(hewan):
    def suara(self):
        print('meong')


# Objek 
k=kucing()
k.suara()
k.bersuara()