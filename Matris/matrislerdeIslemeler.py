import random

yön = ['soldan sağa','şağdan sola','aşağıdan yukarı','yukarıdan aşağı']
orien = enumerate(yön, start=0)#enum tanımı
orientation = list(orien)#enum ı listeye ceviriyoruz yazdırabilmek için
#Soru 1-a
def matris_1(m,n):
    matris1 = []
    for sat in range(m):
        matris1.append([])
        for sut in range(n):
            rand = random.randint(97,122)
            char1 = chr(rand)#burada ascii tablosundaki kucuk a-z arasına ceviriyor
            matris1[sat].append(char1)
    return matris1

#Soru 1-b
def matris_2(satır,sutun,myword,ori):
#önce ori kontrolü yapıyoruz daha sonra verilen karakter matristen buyuk mu diye bakıyoruz
#egerdegilse ori degerine göre matrise işliyoruz
    if(ori>3 or ori<0):
        print("Orientation sınır dışında:",orientation)
    else:
        deneme_1 = matris_1(10,10)
        print("Eski Matris:",deneme_1)
        if(ori == 0):
            if(len(deneme_1[0])-sutun < len(myword)):
                print("Uzun karakter girdiniz.")
            else:
                for i in range(len(myword)):
                    harf = myword[i]
                    deneme_1[satır][sutun]=harf
                    sutun+=1
        if(ori == 1):
            if(sutun < len(myword)):
                print("Uzun karakter girdiniz.")
            else:
                for j in range(len(myword)):
                    harf = myword[j]
                    deneme_1[satır][sutun]=harf
                    sutun-=1
        if(ori == 2):
            if(satır < len(myword)):
                print("Uzun karakter girdiniz.")
            else:
                for k in range(len(myword)):
                    harf = myword[k]
                    deneme_1[satır][sutun]=harf
                    satır-=1
        if(ori == 3):
            if(len(deneme_1)-satır < len(myword)):
                print("Uzun karakter girdiniz.")
            else:
                for l in range(len(myword)):
                    harf = myword[l]
                    deneme_1[satır][sutun]=harf
                    satır+=1
    return deneme_1

#Soru 1-c
def matris_3():
    polidrom_mu=[]
    polid=''
    polid2=''
    deneme_2 = [['p','y','a','a','a','a','a','a','a','a','a','a','y'],
                ['a','t','a','a','a','a','a','a','a','a','t','a','a'],
                ['a','z','a','a','a','a','a','a','a','a','a','z','y'],
                ['a','c','a','a','a','a','a','a','a','a','c','a','y'],
                ['a','y','y','b','b','b','b','b','b','b','b','y','y'],
                ['p','r','a','s','u','k','t','u','u','t','r','a','b']]

    for temp in range(len(deneme_2)):  #bu for satırları geziyor
        for q in range(5,len(deneme_2[0])+1):  #bu for 10 karakter uzunlugunu arttırıyor
            for e in range(0,len(deneme_2[0])+1-q): #bu for aynı satırda stunlar arasında gezmemize yarıyor örn 0+10,1+10,2+10 gibi
                for w in range(0,q):    #bu for ise ilk 10,11,12 sayıyı almamıza yarıyor
                    polid = polid + deneme_2[temp][w+e]     #Sol Sag
                    polid2 = polid2 + deneme_2[temp][-(w+e)-1]      #Sag Sol
                if(polid == polid[::-1]):
                    if(polid not in polidrom_mu):
                        polidrom_mu.append(polid)
                if(polid2 == polid2[::-1]):
                    if(polid2 not in polidrom_mu):
                        polidrom_mu.append(polid2)
                polid=''
                polid2=''

    for temp2 in range(len(deneme_2[0])):
        for q3 in range(3,len(deneme_2)+1):
            for e3 in range(0,len(deneme_2)+1-q3):
                for w3 in range(0,q3):
                    polid += deneme_2[w3+e3][temp2]     #Yukarıdan AS
                    polid2 += deneme_2[-(w3+e3)-1][temp2]       #As Yukarı
                if(polid == polid[::-1]):
                    if(polid not in polidrom_mu):
                        polidrom_mu.append(polid)
                if(polid2 == polid2[::-1]):
                    if(polid2 not in polidrom_mu):
                        polidrom_mu.append(polid2)
                polid=''
                polid2=''
                
    print("Matris:",deneme_2)
    print("Polidromlar:",polidrom_mu)
    polidrom_mu.clear()

def test():
    #test_1 = matris_1(3,3)
    #print("Matris oluşturuldu:",test_1)
    #test_2 = matris_2(2,2,'BARTU',0)
    #print("Matris Degiştirildi:",test_2)
    matris_3()

test()
    