from connect import db, cur

# delete tr_brg
cur.execute("DELETE FROM Tr_Brg WHERE No_Nota = '002' AND Kode_Barang = 'B02'")

# delete Barang
cur.execute("DELETE FROM Barang WHERE Kode_Barang = 'B02'")

# delete Nota
cur.execute("DELETE FROM Nota WHERE No_Nota = '002'")

# delete Supplier
cur.execute("DELETE FROM Supplier WHERE Kode_Supplier = 'S02'")

db.commit()
