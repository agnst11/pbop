from connect import db, cur

# insert data dosen
cur.execute(
    "INSERT INTO Dosen VALUES ('LK1', 'Nopal', 'Cilacap Pride', '0864632638' )")
cur.execute(
    "INSERT INTO Dosen VALUES ('LK2', 'Abel', 'Kutai Pride', '99999999' )")

# insert data Kuliah
cur.execute("INSERT INTO Kuliah VALUES ('')")
