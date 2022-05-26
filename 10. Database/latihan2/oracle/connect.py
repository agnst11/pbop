import cx_Oracle

db = cx_Oracle.connect(
    "latihan2",
    "latihan2",
    "127.0.0.1/XE"
)
cur = db.cursor()

# cur.execute('''CREATE TABLE Dosen (
#     Kode_Dos VARCHAR (3) PRIMARY KEY NOT NULL,
#     Nama_Dos VARCHAR (40),
#     Alamat_Dos VARCHAR (125),
#     No_Telp VARCHAR (15)
#     )''')

# cur.execute('''CREATE TABLE MataKuliah (
#     Kode_MK VARCHAR (3) PRIMARY KEY NOT NULL,
#     Nama_MK VARCHAR (40),
#     SKS VARCHAR (1),
#     Semester VARCHAR (1)
# )''')

# cur.execute('''CREATE TABLE Kuliah (
#     Kode_MK VARCHAR (3),
#     Kode_Dos VARCHAR (3),
#     Waktu VARCHAR (5),
#     Tempat VARCHAR (5),
#     CONSTRAINT fk_kodeDos
#           FOREIGN KEY(KODE_DOS)
#           REFERENCES DOSEN(KODE_DOS),
#     CONSTRAINT fk_kodeMK
#           FOREIGN KEY(KODE_MK)
#           REFERENCES MATAKULIAH(KODE_MK)
#     )''')
