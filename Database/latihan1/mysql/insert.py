from connect import db, cur

# INSERT DATA JABATAN
cur.execute("INSERT INTO `jabatan` VALUES ('D01', 'CEO', 12000000, 5000000)")
cur.execute(
    "INSERT INTO `jabatan` VALUES ('D02', 'SEKRETASRIS', 7000000, 3000000)")
cur.execute("INSERT INTO `jabatan` VALUES ('D03', 'KARYAWAN', 5000000, 1000000)")


# INSERT DATA GOLONGAN
cur.execute(
    "INSERT INTO `Golongan` VALUES ('01', 'Pertama', 500000, 500000, 200000, 100000, 100000)")
cur.execute(
    "INSERT INTO `Golongan` VALUES ('02', 'Kedua', 400000, 400000, 200000, 100000, 100000)")

# INSERT DATA PEGAWAI
cur.execute(
    "INSERT INTO `Pegawai` VALUES ('123456789', 'Danu Dwiki Laksana', 'D01' , '01', 'Punya AYANG', 0)")
cur.execute(
    "INSERT INTO `Pegawai` VALUES ('987654321', 'Nopal Kun', 'D03' , '01', 'Punya AYANG', 0)")


# INSERT DATA GAJI
cur.execute(
    "INSERT INTO `Gaji` VALUES ('Mei', '123456789', 23, 0, 2, 1, 0, 50000)")
cur.execute(
    "INSERT INTO `Gaji` VALUES ('Mei', '987654321', 22, 1, 1, 1, 1, 50000)")


db.commit()
