              Amaliyot
              #1-masala
ismlar=['Sarvar','Doston','Vali','Islom','Diyor']
for ism in ismlar:
     print(f"Salom {ism}, nichiksiz")
print("yaxshi galdingizlami")

               #2-masala
ismlar=['Sarvar','Doston','Islom','Diyor']
for ism in ismlar:
    print(f"Salom {ism}")
print("kod ",len(ismlar),"marta takrorlandi")

               #3-masala
toq_sonlar= (list(range(11,100,2)))
toq_sonlar_kubi=[]
for son in toq_sonlar:
 toq_sonlar_kubi.append(son**3)
print("Bular 10 dan 100 gacha toq sonlar",toq_sonlar)
print("Bular shu toq sonlarning kublari",toq_sonlar_kubi)

               #4-masala
kinolar=[]
print("5 ta eng sevimli kinolaringiz:")
for n in range(5):
 kinolar.append(input(f"{n+1}- kino nomi>>>"))
print("kinolar=",kinolar)

               # 5-masala
odamlar=[]
son=int(input("Bugun necha kishi bn suhbat qildingiz?>>>"))
for n in range(son):
 odamlar.append(input(f"{n+1}- suhbat qilgan odamingiz kim edi:"))
print(odamlar)

                 #6-masala
cars=['toyota','mazda','hyundai','gm','kia']
for car in cars:
  if car=='gm':
   print(car.upper())
  else:
   print(car.title())

                 #7-masala
cars=['toyota','mazda','hyundai','gm','kia']
for car in cars:
  if car!='gm':
   print(car.title())
  else:
   print(car.upper())

                 #8-masala
               # 1-usul:
login=input("Foydalanuvchi loginini kiriting:")
if login=='admin':
 print("Xush kelibsiz,Admin.Foydalanuvchilar ro'yhatini ko'rasizmi?")
else:
 print(f"Xush kelibsiz,{login}!")
                # 2-usul:
login=input("Foydalanuvchi loginini kiriting:").strip().lower()
if login=='admin':
 print("Xush kelibsiz,Admin.Foydalanuvchilar ro'yhatini ko'rasizmi?")
else:
 print(f"Xush kelibsiz,{login}!")

                #9-masala
print("2 ta son kiriting!")
son1=float(input("1-sonni kiriting:"))
son2=float(input("2-sonni kiriting:"))
if son1==son2:
 print("Sonlar teng")
else:
 print("Sonlar teng emas")

                #10-masala
son=float(input("sonni kiriting:"))
if son>0:
 print("Musbat son ")
if son<0:
 print("Manfiy son ")

                #11-masala
son=float(input("sonni kiriting:"))
if son>0:
 print( son**(1/2))
if son<0:
 print("Musbat son kiriting!")








