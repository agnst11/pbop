from connect import db, cur

# update supplier
cur.execute(
    "UPDATE Supplier SET Nama_Supplier = 'Feri Setyawan' WHERE Kode_Supplier = 'S01';")

# update Nota
cur.execute("UPDATE Nota SET Total = 10000000 WHERE No_Nota = '002';")

# update barang
cur.execute(
    "UPDATE Barang SET Nama_Barang = 'VivoBook Duo' WHERE Kode_Barang = 'B02'; ")

# update tr_brg
cur.execute(
    "UPDATE Tr_Brg SET Harga = 12000000 WHERE Kode_Barang = 'B01' AND No_Nota = '001';")


db.commit()
