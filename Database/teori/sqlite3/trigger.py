from tes import cur, db

# table log
cur.execute('''CREATE TABLE IF NOT EXISTS log (
    id INTEGER PRIMARY KEY,
    harga_lama REAL,
    harga_baru REAL, 
    waktu DATE )''')


# create trigger
cur.execute('''CREATE TRIGGER IF NOT EXISTS tr_harga 
                UPDATE OF harga ON produk
                BEGIN
                    INSERT INTO log(
                        harga_lama,
                        harga_baru,
                        waktu)
                    VALUES ( 
                        old.harga, 
                        new.harga,
                        datetime('now'));
                    END;''')

# update harga
cur.execute("UPDATE produk SET harga = ? WHERE kode = ?", (7000, 'P003'))
db.commit()

for row in cur.execute("SELECT * FROM log"):
    print('%d, %.0F, %.0F, %s' % (row[0], row[1], row[2], row[3]))

cur.close()
db.close()
