                #1-masala
# def kopaytma(*sonlar):
#     kopaytma=1
#     for son in sonlar:
#         kopaytma*=son
#     return kopaytma
# print(kopaytma(1,2,3,4,5,6,10))

                 #2-masala
def talabalar(ismi,familiyasi,**malumotlar):
    malumotlar['ismi']=ismi
    malumotlar['familiyasi']=familiyasi
    return malumotlar
talaba=talabalar("Sarvar","Matyoqubov",universitet='SamDu',fakultet='suniy intellekt',yonalish='Dasturiy injinering',kurs=4)
print(talaba)