from connect import db, cur

# update cabang bank
cur.execute(
    "UPDATE CabangBank SET alamatCabang = 'Kab. Pemalang' WHERE kodeCabang = 'PML'")

# update Nasabah
cur.execute(
    "UPDATE Nasabah SET namaNasabah = 'Danu Dwiki Laksana' WHERE idNasabah = 'PML01';")

# update rekening Bank
cur.execute(
    "UPDATE Rekening SET saldo = 20000000 WHERE noRekening = '123456789';")

# update transaksi
cur.execute(
    "UPDATE Transaksi SET jumlah = 10000000 WHERE noTransaksi = 'trx01' AND idNasabah = 'PML01';")

db.commit()
