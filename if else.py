#input
print('Pilih Gerbang kereta')
gerbang = int(input('masukkan gerbang yang dipilih:'))

#proses
if gerbang <= 5 :
    status = 'Benar'
else:
    gerbang = 'Gagal'

#output
print('Gerbang :', gerbang)
print("-----------------")
