class mahasiswa1:
    def __init__(self, nama, nim) -> None:
        self.nama = nama
        self.nim = nim

class mahasiswa2:
    def __init__(self, alamat, jurusan) -> None:
        self.alamat = alamat
        self.jurusan = jurusan

class siswa(mahasiswa1, mahasiswa2):
    def __init__(self, nama, nim, alamat, jurusan) -> None:
        mahasiswa1.__init__(self, nama, nim)
        mahasiswa2.__init__(self,alamat, jurusan)