import os
from colorama import Fore, Style
from penyewaan import sepeda, sewa, admin



s = sepeda
rental = sewa(None,None,None,None,None,None)

while True:
    os.system('cls')
    print('''
> 1. Sewa Sepeda
> 2. Cetak Struk
> 3. Kembalikan
> 4. Login Admin
''')

    menu = input('-> Pilih Menu : ')
    if menu == '1':
        os.system('cls')
        data = s.showItem()
        x = 1
        print('~'*22,'LIST SEPEDA','~'*22)
        print('>\tID \t| Warna \t| Harga Sewa \t| Status \n')
        for i in data:
            print(f'> {x}. {i[0]} \t| {i[1]}  \t| {i[2]}  \t| {i[3]} ')
            x += 1
        pilih = int(input('\n-> Pilih sepeda : '))
        if data[pilih-1][3] == 'rusak':
            print(Fore.RED+'> Maaf sepeda sedang dalam perbaikan'+Style.RESET_ALL)
        
        elif data[pilih-1][3] == 'disewa':
            print(Fore.RED+'> Maaf sepeda sudah disewa'+Style.RESET_ALL)
        
        else:
            nama = input('-> Masukan Nama : ')
            nik = input('-> Masukan NIK : ')
            noHp = input('-> Masukan noHP : ')
            durasi = int(input('-> Durasi Sewa/Jam : '))
            rental = sewa(nama,nik,noHp,data[pilih - 1][0],data[pilih-1][2],durasi)

        input('..')

    elif menu == '2':
        os.system('cls')
        if rental.nik != None:
            rental.cetakStruk()
            print(Fore.GREEN+'> Struk Berhasil dicetak'+Style.RESET_ALL)
            rental = sewa(None,None,None,None,None,None)
        else:
            print(Fore.RED+'> Data sewa tidak tersedia'+Style.RESET_ALL)
            print(Fore.RED+'> Silahkan Isi data pada menu nomor 1'+Style.RESET_ALL)

        input('..')


    elif menu == '3':
        os.system('cls')
        nik = input('-> Masukan NIK : ')
        idSepeda = input('-> Masukan ID Sepeda : ')
        data = rental.cariDataSewa(nik, idSepeda)
        if data != []:
            rental.pembayaran(data[0][4],data[0][5],data[0][6])
            rental.kembalikan(nik, data[0][1], idSepeda)
        else:
            print(Fore.RED+'Data tidak ditemukan'+Style.RESET_ALL)
        input('..')
        

    elif menu == '4':
        os.system('cls')
        nama = input('-> Masukan nama : ')
        password = input('-> Masukan password : ')
        user = admin(nama, password)

        if user._admin__cekAdmin() == True:
            while True:
                os.system('cls')
                print('''> 1. Tambah
> 2. Hapus
> 3. Edit harga
> 4. Edit status
> 5. Keluar
            ''')

                menu = input('-> Pilih Menu : ')
                if menu == '1':
                    os.system('cls')
                    id = input('-> Masukan ID Sepeda : ')
                    warna = input('-> Masukan Warna Sepeda : ')
                    harga = int(input('-> Masukan harga sewa/jam : '))
                    status = input('-> Masukan Status Sepeda (tersedia/disewa/rusak) : ').lower()
                    s.addItem(s,id,warna,harga,status)
                    input('..')

                elif menu == '2':
                    os.system('cls')
                    id = input('-> Masukan ID Sepeda : ')
                    s.delItem(s,id)

                    input('..')

                elif menu == '3':
                    os.system('cls')
                    id = input('-> Masukan ID Sepeda : ')
                    data = s.searchItem(s,id)
                    if data != []:
                        print('\tID \t| Warna \t| Harga Sewa \t| Status \n')
                        print(f'> {data[0][0]} \t| {data[0][1]} \t| {data[0][2]} \t| {data[0][3]} ')
                        harga = int(input('-> Masukan Harga : '))
                        s.updateItem(s,id,harga,'harga')
                    else:
                        print(Fore.RED+'Data tidak ditemukan'+Style.RESET_ALL)

                    input('..')

                elif menu == '4':
                    os.system('cls')
                    id = input('-> Masukan ID Sepeda : ')
                    data = s.searchItem(s,id)
                    if data != []:
                        print('\tID \t| Warna \t| Harga Sewa \t| Status \n')
                        print(f'> {data[0][0]} \t| {data[0][1]} \t| {data[0][2]} \t| {data[0][3]} ')
                        status = input('-> Masukan Status : ')
                        s.updateItem(s,id,status,'status')
                    else:
                        print(Fore.RED+'Data tidak ditemukan'+Style.RESET_ALL)

                    input('..')
                    
                elif menu == '5':
                    break
                else:
                    print('> Menu tidak tersedia')
                    input('..')

        else:
            print('> Anda bukan admin')
            input('')
        

    else: 
        print(Fore.RED+'> Menu tidak tersedia'+Style.RESET_ALL)
        input('..')

