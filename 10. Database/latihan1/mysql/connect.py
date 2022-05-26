import mysql.connector

db = mysql.connector.connect(
    user='root', password='', host='localhost', database='pegawai')
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS jabatan (
    kode_jabatan VARCHAR(3) NOT NULL PRIMARY KEY,
    nama_jabatan VARCHAR(40),
    gapok INTEGER(10),
    tunjangan_jabatan INTEGER(10)
);''')


cur.execute('''CREATE TABLE IF NOT EXISTS Golongan (
	kode_golongan	VARCHAR(2),
	nama_golongan	VARCHAR(10),
	tunjangan_suami	INTEGER(10),
	tunjangan_anak	INTEGER(10),
	uang_makan	INTEGER(10),
	uang_lembur	INTEGER(10),
	akses	INTEGER(10),
	PRIMARY KEY(kode_golongan));''')

cur.execute('''CREATE TABLE IF NOT EXISTS Pegawai (
	nip	VARCHAR(20) NOT NULL,
	nama_pegawai	VARCHAR(40),
	kode_jabatan	VARCHAR(3),
	kode_golongan	VARCHAR(3),
	status	VARCHAR(15),
	jumlah_anak	INTEGER(2),
	PRIMARY KEY(nip),
	FOREIGN KEY (kode_jabatan) REFERENCES jabatan (kode_jabatan),
	FOREIGN KEY (kode_golongan) REFERENCES Golongan (kode_golongan));''')

cur.execute('''CREATE TABLE IF NOT EXISTS Gaji (
	bulan	VARCHAR(20),
	nip	VARCHAR(20),
	masuk	INTEGER(5),
	sakit	INTEGER(5),
	ijin	INTEGER(5),
	alpha	INTEGER(5),
	lembur	INTEGER(5),
	potongan	INTEGER(10),
	FOREIGN KEY(nip) REFERENCES Pegawai (nip));''')
