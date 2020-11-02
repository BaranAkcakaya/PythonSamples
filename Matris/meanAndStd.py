import math
list=[1,12,32,15,92,17,5,53,80,43]

def arit_ort(list):
    toplam=0
    for i in list:
        toplam=toplam+i
        ortalama=toplam/len(list)
    return ortalama

def stand_sapma(list):
    kareTop=arit_ort(list)
    toplam=0
    for i in list:
        toplam+=pow(i-kareTop,2)
    toplam=pow(toplam/(len(list)-1),1/2)
    return toplam

print("ARİTMATİK ORTALAMA: ",arit_ort(list))
print("STANDART SAPMA: ",stand_sapma(list))
