from colorama import Fore, Style
class calculator:
    def __init__(self,a ,b) -> None:
        self.a = a
        self.b =b
        
    def tambah(self):
        return self.a + self.b

    def kurang(self):
        return self.a - self.b

    def kali(self):
        return self.a * self.b
    
    def bagi(self):
        return self.a / self.b


while True:
    reset = False
    a = float(input(Fore.BLUE + '-> Masukan Nilai : ' + Style.RESET_ALL))
    while reset != True:
        print(Fore.CYAN +'''
        1. Tambah
        2. Kurang
        3. Kali
        4. Bagi
        5. Reset\n''' + Style.RESET_ALL)
        
        oper = float(input('Operasi : '))
        if oper == 1:
            b = float(input('-> Masukan Nilai : '))
            calcu = calculator(a,b)
            a = calcu.tambah()
            print(Fore.CYAN + f'Hasil : {a}' + Style.RESET_ALL)
        
        elif oper == 2:
            b = float(input('-> Masukan Nilai : '))
            calcu = calculator(a,b)
            a = calcu.kurang()
            print('Hasil :',a)
        
        elif oper == 3:
            b = float(input('-> Masukan Nilai : '))
            calcu = calculator(a,b)
            a = calcu.kali()
            print('Hasil :',a)
        
        elif oper == 4:
            b = float(input('-> Masukan Nilai : '))
            calcu = calculator(a,b)
            a = calcu.bagi()
            print('Hasil :',a)

        elif oper == 5:
            reset = True