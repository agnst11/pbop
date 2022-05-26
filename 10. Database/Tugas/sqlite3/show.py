from connect import cur

# show data cabang bank
print("Data Cabang Bank")
cur.execute("SELECT * FROM CabangBank")
for row in cur.fetchall():
    print("%s ,%s ,%s" % (row[0], row[1], row[2]))

# show data nasabah
print("\n\nData Cabang Bank")
cur.execute("SELECT * FROM Nasabah")
for row in cur.fetchall():
    print("%s ,%s ,%s" % (row[0], row[1], row[2]))

# show data rekening
print("\n\nData Rekening")
cur.execute("SELECT * FROM Rekening")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))

# show data transaksi
print("\n\nData Transaksi")
cur.execute("SELECT * FROM Transaksi")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))
