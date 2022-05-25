from connect import db, cur

# delete data Dosen
cur.execute("DELETE FROM Dosen WHERE Kode_Dos = 'LK2';")

# delete data kuliah
cur.execute("DELETE FROM Kuliah WHERE Kode_Dos = 'LK2';")

# delete data Mata Kuliah
cur.execute("DELETE FROM MataKuliah WHERE Kode_MK = 'MK3';")

db.commit()
