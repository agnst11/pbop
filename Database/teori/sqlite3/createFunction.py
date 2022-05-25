from tes import db, cur


def toUpper(s):
    return s.upper()


def toLower(s):
    return s.lower()


db.create_function("toUpper", 1, toUpper)
db.create_function("toLower", 1, toLower)


for row in cur.execute("SELECT toUpper(nama) FROM produk"):
    print(row[0])


print('-'*50)

for row in cur.execute("SELECT toLower(nama) FROM produk"):
    print(row[0])

cur.close()
db.close()
