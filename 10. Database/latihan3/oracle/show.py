from connect import cur

# show supplier
print("Data Supplier")
cur.execute("SELECT * FROM Supplier")
for row in cur.fetchall():
    print("%s ,%s" % (row[0], row[1]))

# show nota
print("\n\nData Nota")
cur.execute("SELECT * FROM Nota")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3], row[4]))

# show barang
print("\n\nData Barang")
cur.execute("SELECT * FROM Barang")
for row in cur.fetchall():
    print("%s ,%s" % (row[0], row[1]))

# show tr_brg
print("\n\nData Transaksi Barang")
cur.execute("SELECT * FROM Tr_Brg")
for row in cur.fetchall():
    print("%s ,%s ,%s ,%s" % (row[0], row[1], row[2], row[3]))
