from connect import db, cur

# insert data supplier
cur.execute("INSERT INTO Supplier VALUES ('S01', 'Feri')")
cur.execute("INSERT INTO Supplier VALUES ('S02', 'Zaedar')")

# insert data Nota
cur.execute(
    "INSERT INTO Nota VALUES ('001' ,DATE '2022-05-26', 'Tempo apa', 1000000, 'S01')")
cur.execute(
    "INSERT INTO Nota VALUES ('002', DATE '2022-05-26', 'Tempo bos', 1500000, 'S02')")

# insert barang
cur.execute(
    "INSERT INTO Barang VALUES ('B01', 'TUF GAMING')")
cur.execute(
    "INSERT INTO Barang VALUES ('B02', 'VivoBook 14')")

# insert tr_brg
cur.execute(
    "INSERT INTO Tr_Brg VALUES ('001', 'B01', 2, 16000000)")
cur.execute(
    "INSERT INTO Tr_Brg VALUES ('002', 'B02', 1, 10000000)")

db.commit()
