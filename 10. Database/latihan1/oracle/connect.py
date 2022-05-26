import cx_Oracle

db = cx_Oracle.connect(
    "python",
    "python",
    "127.0.0.1/XE"
)
cur = db.cursor()

# cur.execute('''
#         CREATE TABLE jabatan (
#             kode_jabatan VARCHAR (3) NOT NULL PRIMARY KEY,
#             nama_jabatan VARCHAR (25),
#             gapok INTEGER,
#             tunjangan_jabatan INTEGER
#         )
#         ''')


# cur.execute('''
#         CREATE TABLE Golongan (
#             kode_golongan VARCHAR (2) NOT NULL PRIMARY KEY,
#             nama_golongan VARCHAR (10),
#             tunjangan_suami INTEGER,
#             tunjangan_anak INTEGER,
#             uang_makan INTEGER,
#             uang_lembur INTEGER,
#             akses INTEGER
#         )
#         ''')

# cur.execute('''
#         CREATE TABLE Pegawai (
#             nip	VARCHAR (20) NOT NULL PRIMARY KEY,
#             nama_pegawai VARCHAR (40),
#             kode_jabatan VARCHAR (3),
#             kode_golongan VARCHAR (3),
#             status VARCHAR (15),
#             jumlah_anak INTEGER
#         )
#         ''')

# cur.execute('''
# CREATE TABLE Gaji (
# 	bulan VARCHAR (20),
# 	nip VARCHAR (20),
# 	masuk INTEGER,
# 	sakit INTEGER,
# 	ijin INTEGER,
# 	alpha INTEGER,
# 	lembur INTEGER,
# 	potongan INTEGER
#     )
#     ''')
