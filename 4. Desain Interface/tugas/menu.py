class menuMinuman:
    def __init__(self, nama, deskripsi, harga, gula):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga
        self.__gula = gula


mnm1 = menuMinuman('Jus Jambu', 'Jus jambu merah tanpa gula',
                   8500, 'less Sugar / Normal')
mnm2 = menuMinuman('Jus Alpukat Ori',
                   'Jus alpukat dengan tambahan air gula merah', 15000, 'less Sugar / Normal')
mnm3 = menuMinuman('Jus Alpukat Xtra Milk',
                   'Jus alpukat dengan campuran susu coklat dan tamburan kepingan choco', 15000, 'less Sugar / Normal')
mnm4 = menuMinuman(
    'Red & Smoothie', 'Smoothie pisang susu dan strawberry', 17500, 'less Sugar / Normal')

mnm5 = menuMinuman('Boba Red Velvet',
                   'Minuman Segar disertai boba', 15000, 'less Sugar / Normal')
mnm6 = menuMinuman('Es Teh', 'Minuman Menyegarkan',
                   5000, 'less Sugar / Normal')


pilihanMenu = [mnm1, mnm2, mnm3, mnm4, mnm5, mnm6]
print('Daftar Menu Healthy Fruits')

for i in pilihanMenu:
    print('{} harga Rp. {} , {} , {}' .format(
        i.nama, i.harga, i.deskripsi, i._menuMinuman__gula))
