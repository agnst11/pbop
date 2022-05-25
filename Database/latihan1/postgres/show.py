from connect import db, cur

# show data table pegawai
print("Data Table pegawai")
cur.execute("SELECT * FROM Pegawai")
for row in cur.fetchall():
    print("%s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5]))


# show data table jabatan
print("\n\nData Table Jabatan")
cur.execute("SELECT * FROM jabatan")
for row in cur.fetchall():
    print("%s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3]))


# show data table golongan
print("\n\nData Table Golongan")
cur.execute("SELECT * FROM Golongan")
for row in cur.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

# show data table gaji
print("\n\nData Table Gaji")
cur.execute("SELECT * FROM Gaji")
for row in cur.fetchall():
    print("%s, %s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
