from datetime import datetime
from datetime import time
from penyewaan import sewa

print(time.hour(),':',time.minute())
# rental = sewa(None,None,None,None,None,None)

# # print(datetime.strptime('%Y-%m-%d %H:%M:%S'))
# x = datetime.now()
# time = f"{x.year}-{x.month}-{x.day} {x.hour}:{x.minute}:{x.second}"
# # print(f" {x.year}-{x.month}-{x.day} {x.hour}:{x.minute}:{x.second} ")


# data = rental.cariDataSewa(123456)

# waktuSewa = data[0][6]
# waktuKembali ="2022-5-14 17:00:00"

# durasi = datetime.strptime(f'{waktuKembali}', '%Y-%m-%d %H:%M:%S') - datetime.strptime(f'{waktuSewa}', '%Y-%m-%d %H:%M:%S')

# print(waktuSewa)
# print(int(durasi.seconds / 60))