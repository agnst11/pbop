import psycopg2

db = psycopg2.connect(
    user="postgres",
    password="@d2l",
    host="localhost",
    database="pegawai"
)

cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS jabatan (
    kode_jabatan VARCHAR ( 3 ) PRIMARY KEY NOT NULL,
    nama_jabatan VARCHAR ( 40 ),
    gapok INT,
    tunjangan_jabatan INT );''')


cur.execute('''CREATE TABLE IF NOT EXISTS Golongan (
	"kode_golongan"	VARCHAR(2),
	"nama_golongan"	VARCHAR(10),
	"tunjangan_suami"	INT,
	"tunjangan_anak"	INT,
	"uang_makan"	INT,
	"uang_lembur"	INT,
	"akses"	INT,
	PRIMARY KEY("kode_golongan"));''')

cur.execute('''CREATE TABLE IF NOT EXISTS Pegawai (
	"nip"	VARCHAR(20) NOT NULL,
	"nama_pegawai"	VARCHAR(40),
	"kode_jabatan"	VARCHAR(3),
	"kode_golongan"	VARCHAR(3),
	"status"	VARCHAR(15),
	"jumlah_anak"	INT,
	PRIMARY KEY("nip"),
	FOREIGN KEY ("kode_jabatan") REFERENCES jabatan ("kode_jabatan"),
	FOREIGN KEY ("kode_golongan") REFERENCES Golongan ("kode_golongan"));''')

cur.execute('''CREATE TABLE IF NOT EXISTS Gaji (
	"bulan"	VARCHAR(20),
	"nip"	VARCHAR(20),
	"masuk"	INT,
	"sakit"	INT,
	"ijin"	INT,
	"alpha"	INT,
	"lembur"	INT,
	"potongan"	INT,
	FOREIGN KEY("nip") REFERENCES Pegawai ("nip"));''')

db.commit()
