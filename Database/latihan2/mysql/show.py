from connect import cur


# show data Dosen
print("Tampilkan data Dosen")
cur.execute("SELECT * FROM Dosen")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))

# show data Kuliah
print("\n\nTampilkan data Kuliah")
cur.execute("SELECT * FROM Kuliah")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))

# show data MataKuliah
print("\n\nTampilkan data Mata Kuliah")
cur.execute("SELECT * FROM MataKuliah")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))
