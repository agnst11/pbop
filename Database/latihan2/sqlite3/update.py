from connect import db, cur

# update data Dosen
cur.execute("UPDATE Dosen SET Nama_Dos = 'Naufal' WHERE Kode_Dos = 'LK1';")

# update data Kuliah
cur.execute(
    "UPDATE Kuliah SET Tempat = 'LC2.3' WHERE Kode_MK = 'MK1' AND Kode_Dos = 'LK1';")

# update data mata kuliah
cur.execute(
    "UPDATE MataKuliah SET Nama_MK = 'Rekayasa Web Praktik' WHERE Kode_MK = 'MK1';")

db.commit()
