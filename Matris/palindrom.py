def karakter_kontrol(karakter):
    kontrol=False
    karakter2=karakter[::-1]
    if(karakter2==karakter):
        kontrol=True
    print(kontrol)

karakter_kontrol("iki")
