from connect import cur


# show data Dosen
print("Tampilkan data Dosen")
for row in cur.execute("SELECT * FROM Dosen"):
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))

# show data Kuliah
print("\n\nTampilkan data Kuliah")
for row in cur.execute("SELECT * FROM Kuliah"):
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))

# show data MataKuliah
print("\n\nTampilkan data Mata Kuliah")
for row in cur.execute("SELECT * FROM MataKuliah"):
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))
