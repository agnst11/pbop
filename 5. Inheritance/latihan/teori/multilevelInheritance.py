# Class Parent 
class hewan:
    def bersuara(self):
        print("Kucin Bersuara ")


# child class dari hewan
class kucing(hewan):
    def suara(self):
        print('meong')

# child class dari kucing
class anakKucing(kucing):
    def minum(self):
        print('susu')


k=anakKucing()
k.bersuara()
k.suara()
k.minum()