from connect import db, cur

cur.execute("INSERT INTO produk VALUES ('P001','Pensil',6000)")
cur.execute("INSERT INTO produk VALUES ('P002','Penghapus',9000)")
cur.execute("INSERT INTO produk VALUES ('P003','Penggaris',12000)")

db.commit()
