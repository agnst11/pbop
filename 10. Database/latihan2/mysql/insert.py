from connect import db, cur

# insert data dosen
cur.execute(
    "INSERT INTO Dosen VALUES ('LK1', 'Nopal', 'Cilacap Pride', '0864632638');")
cur.execute(
    "INSERT INTO Dosen VALUES ('LK2', 'Abel', 'Kutai Pride', '99999999');")

# insert data matakuliah
cur.execute("INSERT INTO MataKuliah VALUES ('MK1', 'RWP', '3', '2');")
cur.execute("INSERT INTO MataKuliah VALUES ('MK2', 'MDPL', '3', '2');")
cur.execute("INSERT INTO MataKuliah VALUES ('MK3', 'PBOP', '3', '2');")

# insert data Kuliah
cur.execute("INSERT INTO Kuliah VALUES ('MK1', 'LK1', '10:40', 'LF2.2');")
cur.execute("INSERT INTO Kuliah VALUES ('MK2', 'LK1', '14:40', 'LK2.2');")
cur.execute("INSERT INTO Kuliah VALUES ('MK3', 'LK2', '08:00', 'D3.3');")

db.commit()
