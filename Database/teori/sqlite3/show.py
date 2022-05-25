from tes import db, cur

result = cur.execute("SELECT * FROM produk")

for row in result:
    print('%s, %s, %.0f' % (row[0], row[1], row[2]))

cur.close()
db.close()
