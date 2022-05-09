class menuMinuman:
    def __init__(self, nama, deskripsi, harga):
        self.nama = nama
        self.deskripsi = deskripsi
        self.harga = harga


mnm1 = menuMinuman('Jus Jambu', 'Jus jambu merah tanpa gula', 8500)
mnm2 = menuMinuman('Jus Alpukat Ori',
                   'Jus alpukat dengan tambahan air gula merah', 15000)
mnm3 = menuMinuman('Jus Alpukat Xtra Milk',
                   'Jus alpukat dengan campuran susu coklat dan tamburan kepingan choco', 15000)
mnm4 = menuMinuman(
    'Red & Smoothie', 'Smoothie pisang susu dan strawberry', 17500)


pilihanMenu = [mnm1, mnm2, mnm3, mnm4]
print('Daftar Menu Healthy Fruits')

for i in pilihanMenu:
    print('{} harga Rp. {} , {}'.format(i.nama, i.harga, i.deskripsi))


d = input("masukan makanan : ")

pilihanMenu.insert(d)