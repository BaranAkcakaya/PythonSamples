#Sözlükler de Tuple ve List veri türleri gibi farklı veri türleri bulunduran bulundan 
#mutable(değiştirilebilir) veri türü olduğunu ve süslü parantezlerle gösterilir

sozluk ={"Computer":"Bilgisayar",
"Driver":"Sürücü",
"Memory":"Hafıza",
"Output":"Çıktı",
"Software":["Yazılım","Donanım"],
"Printer":"Yazıcı"}

print(sozluk["Computer"])
print(sozluk["Software"])
print(sozluk["Software"][0])
print(sozluk.keys())
print(sozluk.values())
print(sozluk.items())
