print('hasil ulangan')
nilai = int(input('masukkan nilai: '))

#PROSES
if nilai <80 :
    transkip = "A"
elif nilai > 70 :
    transkip = "B"
elif nilai > 50 :
    transkip = "C"
elif nilai > 30 :
    transkip = "D"
else :
    transkip = "E"

#OUTPUT
print('nilai transkip :', transkip)
print('---------------------------')
