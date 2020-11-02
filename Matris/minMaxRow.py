def satır_hesap(matris):
    liste=[]
    for i in matris:
        toplam=0
        for j in i:
            toplam=toplam+j
        liste.append(toplam)
    e_b=liste[0]
    e_k=liste[0]
    for k in range(len(liste)):
        if(e_b>liste[k]):
            e_b=liste[k]
        if(e_k<liste[k]):
            e_k=liste[k]
    return (e_b,e_k)

def sutun_hesap(matris):
    liste=[]
    for i in range(len(matris[0])):
        toplam=0
        for j in range(len(matris)):
            toplam=toplam+matris[j][i]
        liste.append(toplam)
    e_b=liste[0]
    e_k=liste[0]
    for k in range(len(liste)):
        if(e_b>liste[k]):
            e_b=liste[k]
        if(e_k<liste[k]):
            e_k=liste[k]
    return (e_b,e_k)

matris=[[14,2,33,4],[19,8,7,36],[15,48,68,35],[44,8,456,2]]
x_1=satır_hesap(matris)
x_2=sutun_hesap(matris)
print("En Buyuk Satır ={}  EN Kucuk Satır ={}".format(x_1[1],x_1[0]))
print("En Buyuk Sutun ={}  EN Kucuk Sutun ={}".format(x_2[1],x_2[0]))
        
