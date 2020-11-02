matris=[[1,45,61,2,0],[0,3,4,0,5],[78,4,0,8,1456],[9,7,0,0,45],[48,0,4,5,74]]

def hash_table(matris):
    tablo={}
    counter=0
    for i in matris:
        for j in i:
            tablo[counter]=j
            counter+=1
    print(tablo)
    
def matr_zero_rate(matris):
    counter=0
    for i in matris:
        for j in i:
            if(j==0):
                counter+=1
    rate=counter/(len(matris)*len(matris[0]))
    if(rate<(0.30)):
        hash_table(matris)
    return rate

print("0 Oranı: ",matr_zero_rate(matris))
