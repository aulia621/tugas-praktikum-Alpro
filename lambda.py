def hitung(p,l):
    luas = p*l
    return luas

print("luas tanah(function):",hitung(20,15))

#Lambda
#cara 1: use variabel
luas = lambda p,l : p*l
print("luas tanah (lambda_1):", luas(20,21))

#cara 2: directly
print("luas tanah(lambda_2):", (lambda p,l : p*l)(20,15))
