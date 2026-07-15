 #"While sikli bo'yicha topshiriqlar"
            #1-topshiriq
# rang=input("Svetafor qaysi rangda:?")
# while rang!='qizil' and rang!='yashil' and rang!='sariq':
#     print('Bu hato rang!')
#     rang=input("Qayta kiriting>>")
# print("Rahmat,to'g'ri keladi.")

             #2-topshiriq
import random

tasodifiy_son = random.randint(1, 10)

taxmin = 0

while taxmin != tasodifiy_son:
    taxmin = int(input("1 dan 10 gacha son kiriting: "))

    if taxmin != tasodifiy_son:
        print("Noto'g'ri, qayta urinib ko'ring.")

print("Tabriklaymiz, siz topdingiz!")


               #3-topshiriq
# dostlar=[]
# ism=input("Do'stingizni ismini kiriting(to'xtatish uchun 'stop' bosing)")
# while ism!="stop":
#      dostlar.append(ism)
#      ism=input("Yana ism kiriting(to'xtatish uchun 'stop' bosing)>>")
# print("Do'stlaringiz ro'yhati:")
# print(dostlar)
# for dost in dostlar:
#     print(dost)

               #4-topshiriq
kurs = 12600

while True:
    summa = input("So'm miqdorini kiriting (chiqish uchun 'no' yozing): ")

    if summa.lower() == "no":
        print("Dastur tugadi.")
        break

    summa = float(summa)
    dollar = summa / kurs

    print("Dollar:", round(dollar, 2), "USD")









