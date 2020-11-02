def merhaba(par):
    print("merhaba "+str(par))

merhaba("got")
merhaba(45)

def fib(n):
    a,b=1,1
    while a<n:
        print(a)
        a,b=b,a+b

fib(50)

def fackt(n):
    a=1
    sonuc=1
    while(a<=n):
        sonuc=sonuc*a
        a=a+1
    print(sonuc)

fackt(5)

def fac(n):
    if (n==0):
        return 1
    return n*fac(n-1)

print(fac(5))

def fibo(n):
    if(n==0):
        return 1
    if(n==1):
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(7))

def g(x,y=1):
    return x+5*y
print(g(2,3))
print(g(2))
