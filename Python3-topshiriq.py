                        #List metodlari

# 1).append().--Adds an element at the end of the list(Roʻyxat oxiriga element qoʻshadi)
ismlar=["Sarvar","Doston"]
ismlar.append("Islom")
print(ismlar)
telefonlar=['samsung','vivo','redmi','iphone','honor']
telefonlar.append('nokia')
print(telefonlar)

#2).clear().--Removes all the elements from the list(Roʻyxatdagi barcha elementlarni olib tashlaydi)
telefonlar=['samsung','vivo','redmi','iphone','honor']
telefonlar.clear()
print(telefonlar)
fanlar=['Ona tili','Matematika','ingliz tili','Geografiya','tarix']
fanlar.clear()
print(fanlar)

#3).copy().--Returns a copy of the list(Roʻyxatning nusxasini qaytaradi)
kasblar=["O'qituvchi",'Injiner','Shifokor']
list=kasblar.copy()
print(list)
fanlar=['Ona tili','Matematika','ingliz tili','Geografiya','tarix']
darslik=fanlar.copy()
print(darslik)

#4).count().--Returns the number of elements with the specified value(Belgilangan qiymatga ega elementlar sonini qaytaradi)
meva = ['apple', 'banana', 'cherry','ananas','uzum','cherry']
shu_element_soni = meva.count("cherry")
print(shu_element_soni)
x = meva.count("banana")
print(x)

#5).extend().--Add the elements of a list (or any iterable), to the end of the current list(Joriy roʻyxatning oxiriga roʻyxat elementlarini (yoki har qanday takrorlanadigan) qoʻshing)
meva = ['apple', 'banana', 'cherry','ananas','uzum','cherry']
telefonlar=['samsung','vivo','redmi','iphone','honor']
(meva.extend(telefonlar))
print(meva)
telefonlar=['samsung','vivo','redmi','iphone','honor']
ismlar=["Sarvar","Doston"]
telefonlar.extend(ismlar)
print(telefonlar)

#6).index().--Returns the index of the first element with the specified value(Belgilangan qiymatga ega birinchi element indeksini qaytaradi)
telefonlar=['samsung','vivo','redmi','iphone','honor']
print(telefonlar.index('samsung'))
print(telefonlar.index('redmi'))
meva = ['apple', 'banana', 'cherry','ananas','uzum','cherry']
print(meva.index('cherry'))

#7).insert().--Adds an element at the specified position(Belgilangan joyga element qo'shadi)
mevalar = ['apple', 'banana', 'cherry','uzum','gilos']
mevalar.insert(2, "nok")
print(mevalar)
telefonlar=['samsung','vivo','redmi','iphone','honor']
telefonlar.insert(3, "realmi")
print(telefonlar)

#8).pop().--Removes the element at the specified position(Belgilangan joydagi elementni olib tashlaydi)
mevalar = ['apple', 'banana', 'cherry','uzum','gilos']
meva=mevalar.pop(2)
print(meva)
telefonlar=['samsung','vivo','redmi','iphone','honor']
telefonlar.pop(2)
print(telefonlar)

#9).remove().--Removes the item with the specified value(Belgilangan qiymatga ega elementni olib tashlaydi)
telefonlar=['samsung','vivo','redmi','iphone','honor']
telefonlar.remove(telefonlar[0])
print(telefonlar)
mevalar = ['apple', 'banana', 'cherry','uzum','gilos']
mevalar.remove(mevalar[4])
print(mevalar)

#10).reverse().--Reverses the order of the list(Roʻyxat tartibini oʻzgartiradi)
fanlar=['Ona tili','Matematika','ingliz tili','Geografiya','tarix']
fanlar.reverse()
print(fanlar)
kasblar=["O'qituvchi",'Injiner','Shifokor']
kasblar.reverse()
print(kasblar)

#11).sort().--Sorts the list(Listni tartiblaydi)
mashinalar=['bmw','mersedez benz','volvo','general motors','tesla','audi','matiz','nexia','captiva']
mashinalar.sort()
print(mashinalar)
telefonlar=['samsung','vivo','redmi','iphone','honor']
telefonlar.sort()
print(telefonlar)




