from connect import cur, db

# delete  gaji
cur.execute("DELETE FROM Gaji WHERE nip = '987654321' ;")

# delete pegawai
cur.execute("DELETE FROM Pegawai WHERE nip = '987654321' ;")

# delete golongan
cur.execute("DELETE FROM Golongan WHERE kode_golongan = '02' ;")

# delete jabatan
cur.execute("DELETE FROM jabatan WHERE kode_jabatan = 'D02' ;")

db.commit()
