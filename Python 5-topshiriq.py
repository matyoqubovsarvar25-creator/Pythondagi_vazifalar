#            #For sikli bo'yicha vazifalar
#                   # 1-masala
# # pochtalar=["user1@gmail.com","user2yahoo.com","user3@outlook.com"]
# # for pochta in pochtalar:
# #     if "@" in pochta :
# #         print(f"to'g'ri email: {pochta}")
# #     else:
# #         print(f"noto'g'ri email :{pochta}")
#
#
#                    #2-masala
parollar=["password123", "Qwerty!", "admin", "StrongPass1!"]
maxsus_belgilar=["@%^&*/:!;"]
raqam_bor = False
maxsus_belgi_bor = False
for parol in parollar:
    if len(parol)<8:
        print(f"{parol} ---> qisqa parol")

    for harf in parol:
       if harf.isdigit():
        raqam_bor = True

       if harf in maxsus_belgilar:
        maxsus_belgi_bor = True
        print(f"{parol} Kuchli parol")
    else:
        print(f"{parol} Kuchsiz  parol")

#                     #3-masala
# haroratlar=[20,22, 19, 24, 25, 23, 21]
# for harorat in haroratlar:
#     if harorat>22:
#         print("iliq kun")
#     else:
#         print("salqin kun")
#
#
#                   #4-masala
# menu=['osh','shashlik','manti',"lag'mon"]
# ovqat=input("Nima ovqat buyurtma qilasiz?>>")
# if ovqat.lower() in menu:
#     print("Buyurtmangiz  qabul qilindi.")
# else:
#     print("Kechirasiz,bunday taom yo'q!")
#
#
#                   #5-masala
# yoshlar_royhati=[16, 21, 17,30, 25]
# for yosh in yoshlar_royhati:
#     if yosh <18:
#         print("Yosh chegarasiga yetmagan!")
#     else:
#         print("Xush kelibsiz")
#
#
#                     #6-masala
# xabarlar=["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# for sarlavha in xabarlar:
#     if sarlavha=="Batareya past":
#        print("Telefoningizni quvvatlang")
#     else:
#        print("Sizda o'qilmagan xabar bor")
#
#
#                      #7-masala
# fayllar = ['kitob.jpg', 'ko_ jiguli.mp3', 'tabiat.jpg', 'malohat.mp3', 'iphone16.jpg']
# musiqalar=[ ]
# rasmlar=[ ]
# for fayl in fayllar:
#     if "jpg" in fayl:
#         rasmlar.append(fayl)
#     if "mp3" in fayl:
#         musiqalar.append(fayl)
# print(rasmlar)
# print(musiqalar)
