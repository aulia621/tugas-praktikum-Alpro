#INPUT
print('Hasil Ulangan')
nilai = int(input('masukkan nilai ulangan:'))

#PROSES
if nilai <= 90 :
    status = 'Lulus'
    if nilai >= 95:
        predikat = 'Memuaskan'
    else:
        predikat = 'cukup'
else:
    status = 'Gagal'
    predikat = 'Kurang'

#OUTPUT
print('status :', status)
print('predikat :', predikat)
print("-----------------")

