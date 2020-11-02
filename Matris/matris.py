x=("baran","derya","makas","burda","mizah")
def matris_olustur(kelime,ifade):
    matris=[]
    for i in kelime:
        matris.append(i)
        
    def soldan_saga(ifade):
        for i in matris:
            if(i==ifade):
                return True
        return False

    def sagdan_sola(ifade):
        for i in matris:
            i=i[::-1]
            if(i==ifade):
                return True
        return False

    def yukarıdan_asagı(ifade):
        for i in range(len(matris[0])):
            yeni=''
            for j in range(len(matris)):
                yeni=yeni+matris[j][i]
            if(yeni==ifade):
                return True
        return False

    def asagıdan_yukarı(ifade):
        for i in range(len(matris[0])):
            yeni=''
            for j in range(len(matris)):
                yeni=yeni+matris[j][i]
            yeni=yeni[::-1]
            if(yeni==ifade):
                return True
        return False

    if(soldan_saga(ifade)==True or
       sagdan_sola(ifade)==True or
       yukarıdan_asagı(ifade)==True or
       asagıdan_yukarı(ifade)==True):
        return True
    else:
        return False
    
y="haksj"       
print(y,"->",matris_olustur(x,y))
