import re
def check_password(psw):
    if (len(psw)<8):
        raise  Exception("Parola 8 den kücük")
    elif not re.search("[a-z]",psw):
        raise Exception("kücük harf")
    elif not re.search("[A-Z]",psw):
        raise Exception("büyük harf")
    elif not re.search("[0-9]",psw):
        raise Exception("sayı")
    elif not re.search("[.,_@%]",psw):
        raise Exception("alfanumarik")
    else:
        print("Sifre basarılı")

while True:
    try:
        #check_password("Aasdasddas")
        #check_password("AASDASDŞKŞŞKL")
        #check_password("Aasdasddas99")
        check_password("Aasdasddas99@")
    except Exception as ex:
        print(ex)
    else:
        break

