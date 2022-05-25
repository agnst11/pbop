import psycopg2

db = psycopg2.connect(
    user="postgres",
    password="@d2l",
    host="localhost",
    database="pypg"
)

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS produk (
    kode CHAR(4) NOT NULL PRIMARY KEY,
    nama VARCHAR(25), 
    harga REAL
)''')

db.commit()
