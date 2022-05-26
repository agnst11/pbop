from connect import db, cur

cur.execute("SELECT * FROM produk")


for row in cur.fetchall():
    print('%s, %s, %.0f' % (row[0], row[1], row[2]))

cur.close()
db.close()
