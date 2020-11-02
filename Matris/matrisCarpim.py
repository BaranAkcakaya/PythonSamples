import random

#Soru 1-a
def vektor_olustur(n):
    vektor1=[]
    for a in range(n):
        sayi = random.randint(0,9)
        vektor1.append(sayi)
    return vektor1

#Soru 1-b
def skaler_cap(vek1,vek2):
    if(len(vek1[0]) == len(vek2)):
        toplam = 0
        new_vek=[]
        for j in range(len(vek1)):
            new_vek.append([])
            for n in range(len(vek2[0])):
                for k in range(len(vek1[0])):
                    toplam = toplam + (vek1[j][k] * vek2[k][n])
                new_vek[j].append(toplam)
                toplam = 0
    else:
        print("Bu iki vektör çarpılamaz.")
    return new_vek

#Soru 1-c
def matris_olustur(m,n):
    matris1 = []
    for satır in range(m):
        matris1.append(vektor_olustur(n))
    return matris1

#Soru 1-d
def matris_carp(mat1,mat2):
    if(len(mat1[0]) == len(mat2)):
        new_matris = skaler_cap(mat1, mat2)
    else:
        print("Bu iki matris çarpılamaz.")
    return new_matris

#Soru 1-e
def bes_matris_carp(mat1,mat2,mat3,mat4,mat5):
    carpım1 = matris_carp(mat1,mat2)
    carpım2 = matris_carp(mat3,mat4)
    carpım3 = matris_carp(carpım1,carpım2)
    carpım4 = matris_carp(carpım3,mat5)
    return carpım4

#Soru 1-f sende

#Soru 1-g
def test():
    test1 = vektor_olustur(5)
    print(test1)
    a = matris_olustur(3, 3)
    b = matris_olustur(3, 3)
    c = matris_olustur(3, 3)
    d = matris_olustur(3, 3)
    e = matris_olustur(3, 3)
    
    carpım_1 = matris_carp(a,b)
    print(carpım_1)
    carpım_2 = bes_matris_carp(a,b,c,d,e)
    print(carpım_2)
    
test()
