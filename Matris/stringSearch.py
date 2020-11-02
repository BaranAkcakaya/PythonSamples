def text_search(text,word1):
    check=False
    for word in text.split(' '):
        if word1 in word:
            check=True
            #word_adres(text,word1)
            #return print_text(word1,check)
            print_text(word1,check)
            return word_adres(text,word1)
    else:
        return print_text(word1,check)

def word_adres(text,word):
    liste=[]
    for i in range(len(text)-1):
        if(word==text[i:i+len(word)]):
            liste.append([i,i+len(word)-1])
    return print_word(liste,word)
           #return print(word,"=",[i,i+len(word)-1])

def print_text(word,check):
    print(word,"->",check)

def print_word(liste,word):
    print((liste))
    if(len(liste)==1):
        print(word,"->",liste)
    if(len(liste)>1):
        print(word,"->",end=" ")
        for j in liste:
            print(j[0],end=",")

#text_search("bugun hava cok sıcak","ıca")
text_search("bugun hava cok sıcak","dsaj")
text_search("bugun hava sıcak cok bugun cok sıcak sıcak sıcak sıcak","ıca")
