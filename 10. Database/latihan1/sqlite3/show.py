from connect import db, cur

# show data table pegawai
print("Data Table pegawai")
for row in cur.execute("SELECT * FROM `Pegawai`"):
    print("%s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5]))


# show data table jabatan
print("\n\nData Table Jabatan")
for row in cur.execute("SELECT * FROM `jabatan`"):
    print("%s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3]))


# show data table golongan
print("\n\nData Table Golongan")
for row in cur.execute("SELECT * FROM `Golongan`"):
    print("%s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

# show data table gaji
print("\n\nData Table Gaji")
for row in cur.execute("SELECT * FROM `Gaji`"):
    print("%s, %s, %s, %s, %s, %s, %s, %s" %
          (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
