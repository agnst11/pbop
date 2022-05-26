from tes import db, cur
import csv


with open("excel\produk.csv", 'w', newline='', encoding='utf-8') as csvfile:
    w = csv.writer(csvfile, delimiter=',')
    for row in cur.execute("SELECT * FROM produk"):
        w.writerow(row)

csvfile.close()
cur.close()
db.close()
