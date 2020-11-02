def dekorator(func):
    def alt(ass):
        print("Fonksiyon öncesi")
        func(ass)
        print("Fonksiyon Sonrası")
    return alt
def hello(strName):
    print("Hello World!",strName)

deneme = dekorator(hello)
deneme("Baran")
