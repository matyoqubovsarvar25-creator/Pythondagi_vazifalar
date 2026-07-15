#                    #Lug'at elementlari
#                         #1-masala
otam = {"ismi": "Mavluddin", "yili": 1954,"shahri": "Samarqand"}
print("Otamning ismi", otam["ismi"] + ",", otam["yili"], "-yilda,", otam["shahri"], "shahrida tug'ilgan.")

                         #2-masala
taomlar = {"Otam": "Qozonkabob", "Onam": "Manti","Akam": "Shashlik","Ukam": "grill",  "Men": "somsa"}
print("Otamning sevimli taomi", taomlar["Otam"])
print("Akamning sevimli taomi", taomlar["Akam"])
print("Onamning sevimli taomi", taomlar["Onam"])

#                           #3-masala
lugat = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "if": "Shart",
    "else": "Aks holda",
    "for": "Takrorlash",
    "while": "sikl operatori",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat",
    "dictionary": "Lug'at"
}
print(lugat)

#                           #4-masala
lugat = {
    "int": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "if": "Shart",
    "else": "Aks holda",
    "for": "Takrorlash",
    "while": "sikl operatori",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat",
    "dictionary": "Lug'at"
}
soz = input("Kalit so'zni kiriting: ")
print(lugat[soz])

                            #5-masala
lugat = {
    "int": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "if": "Shart",
    "else": "Aks holda",
    "for": "Takrorlash",
    "while": "sikl operatori",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat"
}
soz = input("Kalit so'z kiriting: ")
if soz in lugat:
    print(soz,"so'zi",lugat[soz],"  deb tarjima qilinadi")
else:
    print("Bunday so'z mavjud emas")