# 1-masala

def foydalanuvchi(ism, familiya, yil, joy, email="", telefon=""):
    yosh = 2026 - yil

    odam = {
        "ismi": ism,
        "familiyasi": familiya,
        "t_yili": yil,
        "yoshi": yosh,
        "joyi": joy,
        "email": email,
        "telefon": telefon
    }

    return odam


ism = input("Ism: ")
familiya = input("Familiya: ")
yil = int(input("Tug'ilgan yil: "))
joy = input("Tug'ilgan joyi: ")
email = input("Email: ")
telefon = input("Telefon: ")

print(foydalanuvchi(ism, familiya, yil, joy, email, telefon))


# 2-masala

def foydalanuvchi(ism, familiya):
    return {
        "ismi": ism,
        "familiyasi": familiya
    }


mijozlar = []

while True:
    ism = input("Ism: ")
    familiya = input("Familiya: ")

    mijozlar.append(foydalanuvchi(ism, familiya))

    javob = input("Yana mijoz qo'shasizmi? (ha/yo'q): ")

    if javob == "yo'q":
        break

print(mijozlar)


# 3-masala

def katta(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c


a = int(input("1-son: "))
b = int(input("2-son: "))
c = int(input("3-son: "))

print("Eng katta son:", katta(a, b, c))


# 4-masala

def aylana(radius):
    return {
        "Radius": radius,
        "Diametr": radius * 2,
        "Perimetr": 2 * 3.14 * radius,
        "Yuza": 3.14 * radius ** 2
    }


r = float(input("Radiusni kiriting: "))

print(aylana(r))


# 5-masala

def tub_sonlar(boshi, oxiri):
    tub = []

    for son in range(boshi, oxiri + 1):
        sanoq = 0

        for i in range(1, son + 1):
            if son % i == 0:
                sanoq += 1

        if sanoq == 2:
            tub.append(son)

    return tub


boshi = int(input("Boshlanish soni: "))
oxiri = int(input("Oxirgi son: "))

print(tub_sonlar(boshi, oxiri))


# 6-masala

def fibonacci(n):
    sonlar = []

    a = 1
    b = 1

    for _ in range(n):
        sonlar.append(a)
        c = a + b
        a = b
        b = c

    return sonlar


n = int(input("Nechta Fibonacci soni kerak: "))

print(fibonacci(n))
