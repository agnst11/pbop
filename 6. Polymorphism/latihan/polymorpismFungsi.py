# Polymorpism dengan fungsi

print(len('Polymorpism')) # Output 12
print(len([1,2,3,4])) # Output 4


# Using Class
class jerman:
    def ibukota(self):
        print('Berlin adalah ibukota negara Jerman')

class jepang:
    def ibukota(self):
        print('Tokyo adalah ibukota neraga Jepang')

negara1 = jerman()
negara2 = jepang()

for country in (negara1, negara2):
    country.ibukota()