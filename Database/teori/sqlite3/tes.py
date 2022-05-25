import sqlite3

with sqlite3.connect('mysql.db') as db:
    cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS produk (
    kode CHAR(4) NOT NULL PRIMARY KEY,
    nama VARCHAR(25), 
    harga REAL
)''')
