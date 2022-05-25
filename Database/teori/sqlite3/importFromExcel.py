from tes import db, cur
import csv

data = [
    ('P004', 'Tinta', 20000),
    ('P005', 'Buku Tulis', 10000),
    ('P006', 'Buku Gambar', 13000)
]

with open("excel\produk1.csv", 'w', newline='', encoding='utf-8') as csvfile:
    w = csv.writer(csvfile, delimiter=',')
    for row in data:
        w.writerow(row)
    csvfile.close()


with open("excel\produk1.csv", 'r', newline='', encoding='utf-8') as csvfile:
    r = csv.reader(csvfile, delimiter=',')
    for row in r:
        cur.execute("INSERT INTO produk VALUES(?,?,?)",
                    (row[0], row[1], row[2],))

db.commit()
csvfile.close()

for row in cur.execute("SELECT * FROM produk"):
    print('%s, %s, %.0f' % (row[0], row[1], row[2]))


cur.close()
db.close()
