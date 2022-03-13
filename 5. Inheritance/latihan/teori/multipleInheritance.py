# parent 1
class perhitungan1:
    def penjumlahan(self, a, b):
        return a+b

# parent 2
class perhitungan2:
    def perkalian(self,a,b):
        return a*b

# child 
class hitung(perhitungan1, perhitungan2):
    def pembagian(self,a,b):
        return a/b


h = hitung()

print(h.pembagian(20, 4))
print(h.penjumlahan(20, 5))
print(h.perkalian(2, 5))