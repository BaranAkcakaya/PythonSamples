# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 14:24:38 2020

@author: lenovoz
"""
#CLASS YAPISI
class Arac:
    def __init__(self,marka,model,plaka):
        self.marka = marka
        self.model = model
        self.plaka = plaka
        
    def yazdır(self):
        print("Upper Class'ı Çağırdınız.")
    
class Araba(Arac):
    marka = ''
    model = ''
    plaka = ''
    hız   = 0
    def __init__(self,marka = 'Ford',model = 'Mustang', plaka = '34BRN34', hız = 300):
        self.marka = marka
        self.model = model
        self.plaka = plaka
        self.hız = hız
    def hızlan(self):
        self.hız += 25
        #print(type(self))
        return self.hız
    
class Ucak(Arac):
    marka = ''
    model = ''
    plaka = ''
    hız   = 0
    def __init__(self,marka = 'BOENG',model = 'AIRBUS', plaka = 'C180', hız = 3000):
        super().__init__(marka, model, plaka)
        self.hız = hız
    def hızlan(self):
        self.hız += 250
        #print(type(self))
        return self.hız
arb = Araba()
arb.marka = 'BMW'
arb.model = 'M6'
arb.plaka = '34YT44'
arb.yazdır()
print("Marka:{},Model:{},Plaka:{},Hız:{}".format(arb.marka,arb.model,arb.plaka,arb.hızlan()))
arb2 = Araba()
arb2.marka = 'Mercedes-Benz'
arb2.model = 'CLA'
arb2.plaka = '34YT565'
arb2.hız   = 175
print("Marka:{},Model:{},Plaka:{},Hız:{}".format(arb2.marka,arb2.model,arb2.plaka,arb2.hız))
arb3 = Araba("AUDI","R8","34KK5214",350)
print("Marka:{},Model:{},Plaka:{},Hız:{}".format(arb3.marka,arb3.model,arb3.plaka,arb3.hız))
uck = Ucak()
uck.marka = 'BOENG'
uck.model = 'AIRBUS200'
uck.plaka = 'FTG420'
uck.hız   = 1500
uck.yazdır()
print("Marka:{},Model:{},Plaka:{},Hız:{}".format(uck.marka,uck.model,uck.plaka,uck.hızlan()))
arc = Arac("None",None,None)
print("Marka:{},Model:{},Plaka:{}".format(arc.marka,arc.model,arc.plaka))

#INHERİTANCE(KALITIM)
"""
class Anne:
    def print_Anne(self):
        print("Anne sınıfının özellikleri")
    def göz(self):
        print("ELA.")
class Baba:
    def print_Baba(self):
        print("Baba sınıfının özellikleri")
    def göz(self):
        print("BLUE.")
class Cocuk(Anne,Baba):
    pass
 
object_d = Cocuk()
object_d.print_Anne()
object_d.print_Baba()
object_d.göz()  #Aynı methoddan iki class da da varsa ilk yazılanınkini alır
"""

class Anne:
 
    def __init__(self):
        self.goz_rengi =  "Yeşil"
        print(self.goz_rengi)
 
    def boyu(self):
        self.boyu = 1.70
        print(self.boyu)
 
class Baba:
    def __init__(self):
        self.goz_rengi = "Siyah"
        print(self.goz_rengi)
 
    def boyu(self):
        self.boyu = 1.86
        print(self.boyu)
 
class Cocuk(Baba,Anne):
    def __init__(self):
        Anne.__init__(self)
 
object_d = Cocuk()
object_d.boyu()

#ENCAPSULATION(KAPsULLEME)
class RegisterCourse:
    #__ koydugumuzda methodu yada degiskeni private yapıyor.
    def __init__(self):
        self.name = "Ahmet"
        self.surname = "Kaleli"
        self.__exam1 = 74
        self.__exam2 = 80
        self.courses = []
 
    def __add(self,course):
        self.courses.append(course)
    def getexam1(self):
        return self.__exam1
    def setexam1(self,nexam1):
        if(nexam1>0 and nexam1<100):
            self.__exam1 = nexam1
 
register = RegisterCourse()
print(register.getexam1())
register.setexam1(95)
print(register.getexam1())


