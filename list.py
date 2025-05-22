#buat list ---> bracket, constructor
myList = [5,7,3]
myList2 = list(('a','b','c'))

#ordered ---> urutan data tetap
print('data : ', myList)
print('data:', myList2)
print('-------------')

#duplicate ---> data ganda
myList = [5,7,3,3]
myList2 = list(('a','b','c'))
print('duplikat :',myList)
print('duplikat :', myList2)
print('--------------')

#index --> 0
# ex : tampilkan nomor index angka 7
myIndex = myList.index(7)
print('index angka 7:', myIndex)
print('----------------')

#change 
#tambah data
#-> append: last,insert: index
myList.append(8)
print('hasil append:', myList)
print('------------')

#ex: tambahkan angka 9 pada index 1
myList.insert(1,9) 
print('hasil append:',myList)
print('-----------------')

#HAPUS DATA
#--> pop:last,remove:specific 
myList.pop()
print('hasil pop:', myList)
print('------------')

#ex: hapus angka 7 dari myList
myList.remove(7)
print('hasil remove:', myList)
print('----------------')

#edit data
#ex: ganti angka 1 dengan 9
myList[1] = 9
print('hasil edit:', myList)
print('----------------')

