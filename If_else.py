# -*- coding: utf-8 -*-
"""
Created on Sun Mar 23 20:51:24 2025

@author: Bekzod
"""
"""
avtolar=['toyota','bmw','mers','gm','tesla','volvo']
for avto in avtolar:
    if avto == 'gm':
        print(avto.upper())
    else:
        print(avto.title())
        


ism =input("Ismingiz nima>>>")
if ism.lower()!='ali':
    print(f"uzur {ism.title()} biz Alini kutyapmiz  ")
else :
    print("salom ,Ali")
    
    
    



javob=float(input("12x6 nechiga teng?>>>"))

if javob!=72:
    print('javob xato')



yosh=int(input("iltimos yoshingizni kiriting.>>>"))

if yosh <18:
    print("kirish mumkin emas")
else:
    print("Xush kelibsiz")
    




login=input("yangi login tanlang>>>")
if len(login)<=5:
    print("login 5 ta belgidan kam bo'lmasligi kerak ")


yosh = int(input("Yoshingiz nechida?>>>"))
if yosh>65: print("Siz COVID-19 risk guruhida ekansiz")


"""

#




"""
avtolar=['toyota','bmw','mers','gm','tesla','volvo']
for avto in avtolar:
    if avto == 'gm':
        print(avto.upper())
    else:
        print(avto.title())




avtolar=['toyota','mazda','gm','mers','bmw']
for avto in avtolar :
    if avto !='gm':
        print(avto.title())
    else:
        print(avto.upper())





ism=input("login ismingizni kiriting>>>")
if ism =="Bekzod":
    print("Xush kelibsiz Admin foydalanuvchilar ro'yxatini ko'rasizmi")
else:
    print(f"Xush leibsiz {ism}")





print("ikkita  son kiriting ")
son1=float(input("1-sonni kiriting"))
son2=float(input("2-sonni kiriting"))

if son1==son2 :
    print("sonlar teng ekan ")
else :
    print("sonlar bir biriga teng emas ")
    
    
    


son=float(input("istalgan son kiriting"))
if son>0:
    print(f"{son} musbat son")

else:
    print(f"{son} manfiy son")
    





son=float(input("istalgan son kiriting>>> "))
if son>0:
    print(f"kvadrat ildizi {son**0.5}ga teng ")

else:
    print("iltimos musbat son kiriting")


son = float(input('Istalgan son kiriting: '))
print(son**(1/2)) if son>0 else print('Musbat son kiriting')


"""