from tes import cur, db

for row in cur.execute("SELECT * FROM produk"):
    print('%s, %s, %.0f' % (row[0], row[1], row[2]))

print('-'*50)

cur.execute("UPDATE produk SET harga = ? WHERE kode = ?", (3000, 'P001'))
db.commit()

for row in cur.execute("SELECT * FROM produk"):
    print('%s, %s, %.0f' % (row[0], row[1], row[2]))

cur.close()
db.close()
