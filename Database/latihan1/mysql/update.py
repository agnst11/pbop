from connect import cur, db

# update data gaji
cur.execute(
    "UPDATE Gaji SET masuk = 20, sakit = 0, ijin = 2 , alpha = 0 WHERE nip = '123456789'")

# update pegawai
cur.execute(
    "UPDATE Pegawai SET nama_pegawai = 'D2L' WHERE nip = '123456789'")


# update Golongan
cur.execute(
    "UPDATE Golongan SET tunjangan_suami = 1000000 WHERE kode_golongan = '01'")

# update jabatan
cur.execute(
    "UPDATE jabatan SET gapok = 15000000 WHERE kode_jabatan = 'D01'")


db.commit()
