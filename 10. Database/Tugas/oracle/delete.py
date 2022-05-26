from connect import db, cur

# delete transaksi
cur.execute(
    "DELETE FROM Transaksi WHERE noTransaksi = 'trx05' AND idNasabah = 'BDG01'")

# delete rekening
cur.execute("DELETE FROM Rekening WHERE noRekening = '987654321' ")

# delete nasabah
cur.execute("DELETE FROM Nasabah WHERE idNasabah = 'BDG01'")

# delete cabang bank
cur.execute("DELETE FROM CabangBank WHERE kodeCabang = 'BDG'")


db.commit()
