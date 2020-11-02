def yetki(page):
    def inner(role):
        if(role == 'Admin'):
            return "{0} roli {1} sayfasına girebilir".format(role,page)
        else:
            return "{0} roli {1} sayfasına giremez".format(role,page)
    return inner

user = yetki("ONLİNE")
print(user("Admin"))
print(user("Kullanıcı"))
