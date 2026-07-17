                 #1-masala
def tugilgan_yil(ism,yosh):
    print(f"Ismingiz:{ism.title()}\nTug'ilgan yilingiz:{2026-yosh}")
ism=input(f"Ismingizni kiriting>>")
yosh=int(input(f"Yoshingizni kiriting>>"))
tugilgan_yil(ism,yosh)

                  #2-masala
def daraja(son):
   print(f"Kvadrati:{son**2}\nKubi:{son**3}")
son=float(input(f"Sonni  kiriting>>"))
daraja(son)

                   #3-masala
def juftmi_toqmi(son):
    if son%2==0:
        print(f"{son}-- Bu son juft")
    else:
        print(f"{son} Bu son toq")
son=float(input('Sonni kiriting>>'))
juftmi_toqmi(son)

                   #4-masala
def taqqoslash(son1,son2):
 if son1==son2:
     print("Sonlar teng")
 elif son1>son2:
     print(f"{son1} soni,{son2} dan katta")
 else:
     print(f"{son2} soni,{son1} dan katta")
son1=float(input("Birinchi sonni kiriting>>"))
son2=float(input("Ikkinchi sonni kiriting>>"))
taqqoslash(son1,son2)

                   #5-masala
def daraja(x,y):
   print(f"{x} ning {y}-darajasi={x**y}")
x=float(input(f"x ning qiymatini kiriting>>"))
y=float(input(f"y ning qiymatini kiriting>>"))
daraja(x,y)

                   #6-masala
def daraja_hisoblash(x):
   print(f"{x} ning 2-darajasi={x**2}")
x=float(input(f"x ning qiymatini kiriting>>"))
daraja_hisoblash(x)

                   #7-masala
def bolinish_alomatlari(x,sonlar):
 for son in sonlar:
      if x%son==0:
          print(f"{x}: {son} ga qoldiqsiz bo'linadi ")
      else:
          print(f"{x}: {son} ga qoldiqsiz bo'linmaydi ")
x=int(input("Sonni kiriting>>"))
sonlar=[2,3,4,5,6,7,8,9,10]
bolinish_alomatlari(x,sonlar)

