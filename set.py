# buat set --> bracket, constructor
myset={'s','e','t',1}
myset2= set(('s','e','t',2))

#unordered --> urutan tidak sama
print('data:',myset)
print('data:',myset2)
print('-------------')

#unduplicate -->unique
myset={'s','e','t',1,1}
myset2= set(('s','e','t',2,2))
print('duplikat:',myset)
print('duplikat:',myset2)
print('-------------')

#unindexed --> tidak memiliki index
#ex:tampilkan index angka 1
myIndex = myset.index(1)
print('index angka 1:', myIndex)
print('------------')

#unchangeable --> tidak dapat dirubah
#ex:ubah angka index 3 dengan 9
myset[3] = 9
print('hasil edit:', myset)
print('------------')

#tambah data --> add
myset.add(5)
print('hasil add:', myset)
print('------------')

#hapus data
#pop:random,remove:spesific
myset.pop()
print('hasil pop:', myset)
print('------------')

#ex:hapus "s" dari myset
myset.remove('s')
print('hasil remove:', myset)
print('------------')








