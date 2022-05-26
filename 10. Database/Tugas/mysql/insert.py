from connect import db, cur

# -- INSERT CabangBank
cur.execute("INSERT INTO CabangBank VALUES ('PML', 'Pemalang', 'Pemalang Jawa Tengah') , ('BDG', 'Bandung', 'Bandung Jawa Barat');")

# -- INSERT Nasabah
cur.execute("INSERT INTO Nasabah VALUES ('PML01', 'Danu', 'Kec. Taman'), ('PML02', 'Adna', 'Kec. Pulosari'), ('BDG01', 'Omy', 'Kec. Hulubanteng');")

# -- INSERT Rekening
cur.execute("INSERT INTO Rekening VALUES ('123456789', '123456', 'PML01', 'PML', 12000000), ('234567891', '234567', 'PML02', 'PML', 10000000), ('987654321', '654321', 'BDG01', 'BDG', 50000000);")

# -- INSERT Transaksi
cur.execute("INSERT INTO Transaksi VALUES ('trx01' , 'Gold', 'PML01', date('now'), 8000000), ('trx05' , 'Platinum', 'BDG01', date('now'), 30000000);")


# commit database
db.commit()
