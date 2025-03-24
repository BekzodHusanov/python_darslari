# -*- coding: utf-8 -*-
"""
Created on Mon Mar 24 08:44:51 2025

@author: Bekzod 
"""
"""
yosh =int(input("yoshingizni kiriting >>>"))
if yosh<=4:
    print("sizga kirish bepul")
elif yosh <= 12:
    print("sizga kirish 4000 so'm ")
else:
    print("sizga kirish 10000 so'm")





yosh =int(input("yoshingizni kiriting >>>"))
if yosh<=4:
    narh=0
elif yosh <= 12:
    narh=4000
else:
    narh=8000
print(f"salom sizga kirish {narh}so'm")







yosh =int(input("yoshingizni kiriting >>>"))
if yosh<=4:
    narh=0
elif yosh <= 12:
    narh=4000
elif yosh <65:
    narh=1000
elif yosh <85:
    narh=500
else:
    narh=0
print(f"salom sizga kirish {narh}so'm")






kun =input("bugun qaysi kun?>>>")
if kun.lower()=="shanba" or kun.lower()=="yakshanba":
    print("Bugun dam olish kuni ")
else:
    print("Bugun ish kuni ")
    





pul=int(input("qancha puling bor ?>>>"))

kun= input("Bugun qaysi kun >>>")

if kun.lower()=="shanba" and pul==1200:
    print("sen velosped olgani bozorga borsang boladi")
else :
    print("uyda o'tir ")








narh= 15000
salat=1
choy=0
asarti=1
qaymoq=1

if choy:
    print("mijoz choy oldi")
    narh=narh+3000
if salat:
    print("mijoz salat oldi ")
    narh=narh+4000
if asarti:
    print("mijoz asarti oldi ")
    narh=narh+10000
if qaymoq :
    print("mjoz qaymoq oldi ")
    narh=narh+5000
print(f"jami narh {narh}so'm ")





taomlar=['manti','osh','shashlik','qaymoq']

taom=input("siz nima ovqat yeyishni xoxlaysiz>>>")

if taom.lower() in taomlar:
    print("buyurtma qabul qilindi ")
else:
    print("afsuski bizda bunday taom yoq ")







menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

for taom in buyurtmalar:
    if taom in menu:
        print(f"Menuda {taom} bor")
    else:
        print(f"Kechirasiz, menuda {taom} yo'q")








menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = ["osh","somsa","manti", "shashlik"]

if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"bizda {taom} bor ")
        else:
            print(f"bizda quydagi {taom} yo'q ")
else:
    print("savatchangiz bo'sh ")



"""

# Amalyot  

"""
juft_son=int(input("Juft son kiriting >>> "))


if juft_son==0:
    print("0 juft ham toq ham emas ")
elif juft_son%2==0:
    print("rahmat !")

else:
    print("Bu son juft emas ")




yosh =int(input("yoshingiz nechida ?>>>"))

if yosh<4 or yosh >60 :
    narh=0
elif yosh <=18 :
    narh=10000
elif yosh >18:
    narh=20000
print(f"sizga kirish {narh}so'm ")








son1= float(input("1-sonni kiriting >>>"))

son2=float(input("2-sonni kiriting >>>"))

if son1==son2:
    print(f"{son1}={son2}")
elif son1>son2:
    print(f"{son1}>{son2}")
else:
    print(f"{son1}<{son2}")





mahsulotlar =['chelak','suv','sandiq','qoshiq','qozon']

savat=[]

for n in range(5):
    savat.append(input(f"savatga {n+1}-mahsulotni qo'shing "))

for mahsulot  in savat:
    if mahsulot.lower() in mahsulotlar:
        print(f"do'konimizda {mahsulot}  bor")
    else: 
        print(f"do'konimizda {mahsulot} yo'q ")






mahsulotlar =['chelak','suv','sandiq','qoshiq','qozon']

savat=[]

for n in range(5):
    savat.append(input(f"savatga {n+1}-mahsulotni qo'shing "))
    
bor_mahsulot=[]

mavjud_emas=[]


for mahsulot  in savat:
    if mahsulot.lower() in mahsulotlar:
        bor_mahsulot.append(mahsulot)
  
    else:
        mavjud_emas.append(mahsulot)

if  mahsulot in mavjud_emas:
    print("Do'konimizda yo'q  mahsulotlar :")
    
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("do'konimizda barcha mahsulotlar bor ")
    
    

foydalanuvchilar = ['alijon','anvar','suxrob','bekzod','umidjon']

login=input("Yangi  login tanlang >>>")

if login in foydalanuvchilar:
    print("Login band, yangi login tanlang")
else:
    print(f"Xush kelibsiz  {login.title()} ")


  

son =int(input("Istalgan butun son kiriting >>>"))   

for n in range(2,11):
    if son%n==0:
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi ")

    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        









