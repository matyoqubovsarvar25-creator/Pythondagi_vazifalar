#      2-dars.Topshiriqlar
#
#           1-misol
# son=int(input("Sonni kiriting:"))
# kv=son**2
# print("Shu sonning kvadrati",kv,"ga teng")
# kub= son**3
# print("Shu sonning kubi",kub,"ga teng")
#
#           2-misol
# yosh=int(input("yoshingiz nechada:"))
# yili=2026-yosh
# print(yosh)
# print("Siz "+str(yili)+"- yil ekansiz")
#
#             3-misol
# son1=int(input("1-sonni kiriting:"))
# son2=int(input("2-sonni kiriting:"))
# print(son1)
# print(son2)
# yigindi=son1+son2
# print("yig'indisi=",yigindi)
# ayirma=son1-son2
# print("ayirmasi=",ayirma)
# kopaytma=son1*son2
# print("ko'paytmasi=",kopaytma)
# bolinma=son1/son2
# print("bo'linmasi=",bolinma)


#https://www.w3schools.com/python/python_strings_methods.asp

 # 1).capitalize().--Converts the first character to upper case(Birinchi belgini bosh harfga aylantiradi)
# matn1=input("1-matnni kiriting::")
# print(matn1.capitalize())
# matn2=input("2-matnni kiriting::")
# print(matn2.capitalize())

#2).casefold().--Converts string into lower case(Satrni kichik harfga aylantiradi)
# soz1=input("1-so'zni kiriting::")
# print(soz1.casefold())
# soz2=input("2-so'zni kiriting::")
# print(soz2.casefold())

#3).center().--Returns a centered string(Markazlangan satrni qaytaradi)
# matn1="salom"
# print(matn1.center(10,"*"))
# matn2="nichik"
# print(matn2.center(20,"."))


#4).count().--Returns the number of times a specified value occurs in a string(Belgilangan qiymat satrda necha marta sodir bo'lishini qaytaradi)
# matn="bugun soat o'n birda dars bor.Dars  nechada"
# print(matn.count("b"))
# matn2=input("matnni kiriting:")
# print(matn)
# print("Matnda a harfi",matn.count("a"),"marta uchraydi")


#5).encode().--Returns an encoded version of the string(Satrning kodlangan versiyasini qaytaradi)
# matn2 = "Hello world"
# print(matn2.encode())
# matn="My name is Ståle"
# print(matn.encode())

#6).endswith().--Returns true if the string ends with the specified value(Agar satr belgilangan qiymat bilan tugasa, true qiymatini qaytaradi)
# matn="salom,qanday"
# print(matn.endswith("qanday"))
# matn2="Nagap,jollimison.Ishla yaxshimi"
# print(matn2.endswith("jollimison"))


#7).expandtaps().--Sets the tab size of the string(Satrning yorliq o'lchamini o'rnatadi)
# soz="H\te\tl\tl\to"
# print(soz)
# soz2="W\to\tr\tl\td"
# print(soz2)

#8).find().--Searches the string for a specified value and returns the position of where it was found(Satrdan ko‘rsatilgan qiymatni qidiradi va uning topilgan o‘rnini qaytaradi.)
# matn="Bugun Urganchda havo bulutli"
# print(matn.find("havo"))
# matn="Salom,nichiksiz.Oydinmisiz"
# print(matn.find("nichiksiz"))

#9).format().--Formats specified values in a string(Satrdagi belgilangan qiymatlarni formatlaydi)
# matn="Bu mahsulot faqat {price:.2f} so'mga sotiladi"
# print(matn.format(price=300000))
# matn2="Faqat {price:.2f} dollarga!"
# print(matn2.format(price=15))

#10).format_map().--Formats specified values in a string(Satrdagi belgilangan qiymatlarni formatlaydi)
# matn="Bu mahsulot faqat {price:.2f} so'mga sotiladi"
# print(matn.format_map({"price":300000}))
# matn2="Faqat {price:.2f} dollarga!"
# print(matn2.format_map({"price":15}))

#11).index().--Searches the string for a specified value and returns the position of where it was found(Belgilangan qiymat uchun satrni qidiradi va u topilgan joyni qaytaradi)
# matn1="Salom,xush kelibsiz"
# print(matn1.index("kelibsiz"))
# matn2="Salom,xush kelibsiz"
# print(matn2.index("xush"))

#12).isalnum().--Returns True if all characters in the string are alphanumeric(Agar satrdagi barcha belgilar alfanumerik bo'lsa, True qiymatini qaytaradi)
# ism="Sarvar"
# print(ism.isalnum())
# ism2="Sarvar 123"
# print(ism2.isalnum())

#13).isalpha()	Returns True if all characters in the string are in the alphabet(Agar satrdagi barcha belgilar alifboda bo'lsa, True qiymatini qaytaradi)
# kompaniya="Summer TEch"
# print(kompaniya.isalpha())
# kompaniya="SummerTEch"
# print(kompaniya.isalpha())

#14).isascii().--Returns True if all characters in the string are ascii characters(Agar satrdagi barcha belgilar ascii belgilar bo'lsa, True qiymatini qaytaradi)
# text="asci234"
# print(text.isascii())
# text2="asci `' !#.-)234"
# print(text2.isascii())

#15).isdecimal().--Returns True if all characters in the string are decimals(Agar satrdagi barcha belgilar oʻnli kasr boʻlsa, True qiymatini qaytaradi)
# matn="kompyuter"
# print(matn.isdecimal())
# son="5"
# print(son.isdecimal())

#16).isdigit().--Returns True if all characters in the string are digits(Agar satrdagi barcha belgilar raqam bo'lsa, True qiymatini qaytaradi)
# matn="kompyuter"
# print(matn.isdigit())
# son="5"
# print(son.isdigit())

#17).isidentifier().--Returns True if the string is an identifier(Agar satr identifikator bo‘lsa, True qiymatini qaytaradi)
# matn="demo"
# print(matn.isidentifier())
# matn2="real shot"
# print(matn2.isidentifier())

#18).islower().--Returns True if all characters in the string are lower case(Agar satrdagi barcha belgilar kichik bo'lsa, True qiymatini qaytaradi)
# matn="Kompyuter texnologiyalar"
# print(matn.islower())
# matn2="kompyuter texnologiyalar"
# print(matn2.islower())

#19).isnumeric().--Returns True if all characters in the string are numeric(Agar satrdagi barcha belgilar raqamli bo'lsa, True qiymatini qaytaradi)
# matn="Bugun soat 11 da dars bor"
# print(matn.isnumeric())
# matn2="11"
# print(matn2.isnumeric())

#20).isprintable().--Returns True if all characters in the string are printable(Agar satrdagi barcha belgilar chop etilishi mumkin bo'lsa, True qiymatini qaytaradi)
# satr="Hello"
# print(satr.isprintable())
# matn="H\ne\nl\nl\no"
# print(matn.isprintable())

#21).isspace().--Returns True if all characters in the string are whitespaces(Agar satrdagi barcha belgilar boʻsh joy boʻlsa, True qiymatini qaytaradi)
# matn="   "
# print(matn.isspace())
# matn2=" Sarvar "
# print(matn2.isspace())

#22).istitle().--Returns True if the string follows the rules of a title(Agar satr sarlavha qoidalariga rioya qilsa, True qiymatini qaytaradi)
# gap="Salom Men Sarvarbek"
# print(gap.istitle())
# gap2="Salom men Sarvarbek"
# print(gap2.istitle())

#23).isupper().--Returns True if all characters in the string are upper case(Agar satrdagi barcha belgilar bosh harflar bo‘lsa, True qiymatini qaytaradi)
# matn="ASUS VIVOBOOK"
# print(matn.isupper())
# matn2="Asus vivobook"
# print(matn2.isupper())

#24).join().--Joins the elements of an iterable to the end of the string(Takrorlanuvchi elementlarni satr oxirigacha birlashtiradi)
# ismlar=("Sarvar","Doston","Vali")
# print("#".join(ismlar))
# hayvonlar=("it","mushuk","qo'y")
# print("uy hayvonlari-","*".join(hayvonlar))

#25).ljust().--Returns a left justified version of the string(Satrning chapga asoslangan versiyasini qaytaradi)
# meva="Olma"
# print(meva.ljust(6),"--Bu men eng yoqtirgan meva")
# text="mushuk"
# print(text.ljust(15),"=uy hayvoni")

#26).lower().--Converts a string into lower case(satrni kichik harfga o'zgartiradi)
# txt="Hello World"
# print(txt.lower())
# txt2="HOW ARE YOU?"
# print(txt2.lower())

#27).lstrip().--Returns a left trim version of the string(Satrning chap tomondagi bo‘sh joylari olib tashlangan variantini qaytaradi)
# matn="      Men yangi 📞📞📲oldim       "
# print(matn.lstrip())
# matn2="                      Hayrli tong"
# print(matn2.lstrip())

#28).maketrans().--Returns a translation table to be used in translations(Tarjimalarda foydalaniladigan tarjima jadvalini qaytaradi)
# txt="Hello Jae"
# new_txt=str.maketrans("a","o")
# print(txt.translate(new_txt))
# matn = "Good night Sam!"
# x = "mSa"
# y = "eJo"
# z = "odnght"
# mytable = str.maketrans(x, y, z)
# print(matn.translate(mytable))

#29).partition().--Returns a tuple where the string is parted into three parts(Satrni uch qismga ajratuvchi kortejni qaytaradi)
# matn="Keling shu kodlarning natijasini ko'ramiz:"
# print(matn.partition("kodlarning"))
# matn2="Python dasturlash kursi"
# print(matn2.partition("tili"))

#30).replace().--Returns a string where a specified value is replaced with a specified value(Belgilangan qiymat boshqa bir belgilangan qiymat bilan almashtirilgan satrni qaytaradi)
# matn="O'zbekistonning poytaxti Toshkent"
# print(matn.replace("Toshkent","Samarqand"))
# matn="Hello world"
# print(matn.replace("Hello world","Salom,Sarvarbek"))

#31).rfind().--Searches the string for a specified value and returns the last position of where it was found(Satrdan ko‘rsatilgan qiymatni izlaydi va uning oxirgi topilgan o‘rnini qaytaradi.)
# matn="O'zbekistonning poytaxti Toshkent"
# print(matn.rfind("Toshkent"))
# matn2="Hello world"
# print(matn2.rfind("l"))


#32).rindex().--Searches the string for a specified value and returns the last position of where it was found(Satrdan belgilangan qiymatni izlaydi va u topilgan oxirgi o‘rinni qaytaradi.)
# matn="O'zbekistonning poytaxti Toshkent"
# print(matn.rindex("Toshkent"))
# matn2="Hello world"
# print(matn2.rindex("l"))

#33).rjust().--Returns a right justified version of the string(Satrning o‘ngga tekislangan variantini qaytaradi)
# soz = "apple"
# matn = soz.rjust(5)
# print(matn, "is my favorite fruit.")
# matn="Toshkent"
# matn2=matn.rjust(29)
# print(matn2, "O'zbekistonning poytaxti")

#34).rpartition().--Returns a tuple where the string is parted into three parts(Satrni uch qismga ajratuvchi kortejni qaytaradi)
# matn="O'zbekistonning poytaxti Toshkent"
# print(matn.rpartition("poytaxti"))
# matn2="Python dasturlash kursi"
# print(matn2.rpartition("kurs"))

#35).rsplit().--Splits the string at the specified separator, and returns a list(Satrni ko‘rsatilgan ajratgich bo‘yicha ajratadi va ro‘yxat qaytaradi.)
# mevalar="olma,uzum,nok,anor"
# new=mevalar.rsplit(",")
# print(new)
# mevalar2="banan,ananas,kivi,olcha"
# yangi_meva=mevalar2.split(",",1)
# print(yangi_meva)

#36).rstrip().--Returns a right trim version of the string(Satrning o‘ng tomondagi bo‘sh joylari olib tashlangan variantini qaytaradi)
# matn="O'zbekistonning poytaxti Toshkent             "
# print(matn.rstrip())
# matn2="Hello world          "
# print(matn2.rstrip())

#37).split().--Splits the string at the specified separator, and returns a list(Satrni ko‘rsatilgan ajratgich bo‘yicha ajratadi va ro‘yxat qaytaradi.)
# mevalar="olma,uzum,nok,anor"
# new=mevalar.split(",")
# print(new)
# mevalar2="banan,ananas,kivi,olcha"
# yangi_meva=mevalar2.split(",",1)
# print(yangi_meva)

#38).splitlines().--Splits the string at line breaks and returns a list(Satrni qator ajratgichlari bo‘yicha ajratadi va ro‘yxat qaytaradi)
# txt = "Thank you for the music\nWelcome to the jungle"
# print(txt.splitlines())
# txt2="Thank you for the \nmusic Welcome to the jungle"
# print(txt2.splitlines())

#39).startswith().--Returns true if the string starts with the specified value(Agar satr ko‘rsatilgan qiymat bilan boshlansa, true qaytaradi)
# txt = "Thank you for the music\nWelcome to the jungle"
# print(txt.startswith(" you for"))
# txt2="Thank you for the music\nWelcome to the jungle"
# print(txt2.startswith("Thank"))

#40).strip().--Returns a trimmed version of the string(Satrning chetlaridagi bo‘sh joylar olib tashlangan variantini qaytaradi)
# matn="      Men yangi 📞📞📲oldim        "
# print(matn.strip())
# meva="    gilos      "
# yangi=meva.strip()
# print("Menga",yangi," mevasi juda yoqadi")

#41).swapcase().--Swaps cases, lower case becomes upper case and vice versa(Harflar registrini almashtiradi: kichik harflar katta harflarga, katta harflar esa kichik harflarga o‘tkaziladi.)
# matn=" Men yangi 📞📞📲oldim "
# print(matn.swapcase())
# txt = "Hello My Name Is PETER"
# x = txt.swapcase()
# print(x)

#42).title().--Converts the first character of each word to upper case(Har bir so‘zning birinchi belgisini bosh harfga aylantiradi)
# matn="sarvar,doston,valijon"
# print(matn.title())
# txt = "Welcome to my 2nd world"
# print(txt.title())

#43).translate().--Returns a translated string(Tarjima qilingan satrni qaytaradi)
# mydict = {87: 86}
# txt = "Hello World"
# print(txt.translate(mydict))
# txt2 = "Hello World!"
# mytable = str.maketrans("d", "T")
# print(txt.translate(mytable))

#44).upper().--Converts a string into upper case(Satrni bosh harflarga o‘tkazadi)
# satr="Hello my friend!"
# print(satr.upper())
# matn="O'zbekistonning poytaxti Toshkent"
# print(matn.upper())

#45).zfill().--Fills the string with a specified number of 0 values at the beginning(Satrning boshiga belgilangan miqdordagi 0 qiymatlarini qo‘shib to‘ldiradi)
car="jentra"
print(car.zfill(20))
matn="ASUS Vivobook"
print(matn.zfill(14))


