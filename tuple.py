# create --> bracket,constructor
myTuple = ('alif',83)
myTuple2 = tuple(('alif','alfy'))

#ordered --> urutan data tetap
print('data:', myTuple)
print('data:', myTuple2)

#Duplicate
myTuple = ('alif',83.83)
myTuple2 = tuple(('alif','alfy','aylif'))
print('duplikat:', myTuple)
print('duplikat : ', myTuple2)
print('-----------')

#index --.0
#ex: tampilkan no index angka 83
myIndex= myTuple.index(83)
print('index angka 83:', myIndex)
print('----------')

#unchangeable
#ex: ubah data index 1 dengan 90
myTuple[1]= 90
print('hasil edit:', myTuple)
print('----------')
