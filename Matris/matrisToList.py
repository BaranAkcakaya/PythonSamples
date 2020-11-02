dict_type={0:0,1:2,2:0,3:7,4:0,5:0,6:0,7:3,8:0}

def diziye_aktar(d_t):
    dizi=[]
    counter=0
    for i in range(3):
        dizi.append([])
        for j in range(3):
            dizi[i].append(d_t.get(counter))
            print(dizi[i])
            counter+=1
    return dizi

def yazdır(dizi):
    for i in dizi:
        print(i)

liste=diziye_aktar(dict_type)
yazdır(liste)
