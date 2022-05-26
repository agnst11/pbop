import cx_Oracle

db = cx_Oracle.connect(
    "latihan3",
    "latihan3",
    "127.0.0.1/XE"
)
cur = db.cursor()

# cur.execute('''CREATE TABLE Supplier (
# 	Kode_Supplier VARCHAR (3) PRIMARY KEY NOT NULL,
# 	Nama_Supplier VARCHAR (40) )''')

# cur.execute('''CREATE TABLE Nota (
# 	No_Nota VARCHAR (3) PRIMARY KEY,
# 	Tanggal date,
# 	Tempo VARCHAR (10),
# 	Total INTEGER,
# 	Kode_Supplier VARCHAR (3),
#     CONSTRAINT fk_kodeSupplier
#     FOREIGN KEY(Kode_Supplier)
#     REFERENCES Supplier(Kode_Supplier)
#     )''')

# cur.execute('''CREATE TABLE Barang (
# 	Kode_Barang VARCHAR (3) PRIMARY KEY NOT NULL,
# 	Nama_Barang VARCHAR (40) )''')

# cur.execute('''CREATE TABLE Tr_Brg (
# 	No_Nota VARCHAR (3),
# 	Kode_Barang VARCHAR (3),
# 	Qty INTEGER,
# 	Harga INTEGER,
#     CONSTRAINT fk_noNota
# 	    FOREIGN KEY(No_Nota)
#         REFERENCES Nota(No_Nota),
#     CONSTRAINT fk_kodeBarang
# 	    FOREIGN KEY(Kode_Barang)
#         REFERENCES Barang(Kode_Barang))
#     ''')
