#arguman listesi oluturrma
def bastır(*a):      #burda a yı bır dızıymıs gıbı alıyor
    print (a)
    for i in a:
        print(i)

bastır(1,2,3,4,5,6)
bastır(1,2,3,4)
bastır(1)

def toplam(*b):
    sonuc=0
    for i in b:
        sonuc+=i
    return sonuc

print(toplam(2,3))
print(toplam(1,2,3,4,5,6,7,8,9))
print(toplam(9,8,7))

def toplama(basla,*c):
    sonuc=basla
    print("baslangıc:"+str(basla))
    for i in c:
        sonuc+=i
    return sonuc
print(toplama(2,3,4,5))

def fonk1(**a):
    for i in a:
        print( str(i)+str(a[i]))


fonk1(a=2,b=3,c=4)
