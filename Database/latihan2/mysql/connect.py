import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="uteyeah"
)

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Dosen (
    Kode_Dos VARCHAR(3) PRIMARY KEY NOT NULL,
    Nama_Dos VARCHAR(40),
    Alamat_Dos VARCHAR(125),
    No_Telp VARCHAR(15)
    );''')

cur.execute('''CREATE TABLE IF NOT EXISTS MataKuliah (
    Kode_MK VARCHAR(3) PRIMARY KEY NOT NULL,
    Nama_MK VARCHAR(40),
    SKS VARCHAR(1),
    Semester VARCHAR(1)    
);''')

cur.execute('''CREATE TABLE IF NOT EXISTS Kuliah (
    Kode_MK VARCHAR(3) ,
    Kode_Dos VARCHAR(3),
    Waktu TIME,
    Tempat VARCHAR(5),
    FOREIGN KEY(Kode_Dos) REFERENCES Dosen (Kode_Dos),
    FOREIGN KEY(Kode_MK) REFERENCES MataKuliah (Kode_MK)
    );''')
