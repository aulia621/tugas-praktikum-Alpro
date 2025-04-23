#funtion 1
def tanah(panjang,lebar):
    luas = panjang * lebar
    return luas

#function 2
def harga(luas,hpm):
    jual = luas * hpm 
    print('harga jual tanah:',jual)
    print('-----------------------')

luas = tanah(5,3)
harga(luas,1000)