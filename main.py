for i in range(2, 10):
    print(i)

lista = ['Sör', 'Bor', 'Palinka']
print(len(lista))

for i in lista:
    print(i)

for i in range(3):
    print(i)
    for j in range(3):
        print(j)

for i in range(10):
    if i == 5:
        break
    print(i)

    for i in range(10):
        if i == 5:
            continue
        print(i)

i = 1
while i < 5:
    print(i)
    i += 1

while True:
    szam = int(input("Adj meg egy számot:"))
    print("A szám:", szam)
    if szam == 0 :
        break
    print("A program véget ért")

szamlalo = 0
while True:
    szamlalo += 1
    if szamlalo %2 == 0:
        continue
    print(szamlalo)
    if szamlalo >20:
        break

import random
while True:
    input("Nyomj egy ENTER-t a kocka dobásához")
    dobas = random.randint(1,6)
    print(f"{dobas}-t dobtál")
    ujdobas = input("Szeretnél újra dobni?(i/n)")
    if ujdobas == 'n':
        break

while True:
    oldal = int(input("Hány oldalu kockával akarsz dobni?"))
    dobas = random.randint(1, oldal)
    print(f"{dobas}-t dobtál")
    ujdobas = input("Szeretnél újra dobni?(i/n)")
    if ujdobas == 'n':
        break

elso_jatekos = input("Első jatekos neve")
masodik_jatekos = input("Masodik jatekos neve")

elso_osszeg = 0
masodik_osszeg = 0

print(elso_jatekos +"dobasai következnek")
dobas = random.randint(1,6)
print("1.kocka:",dobas)
elso_osszeg = elso_osszeg+dobas
dobas = random.randint(1,6)
print("2.kocka:",dobas)
elso_osszeg = elso_osszeg+dobas
print("a 2 kocka dobasanak az osszege", elso_osszeg)


print(masodik_osszeg +"dobasai következnek")
dobas = random.randint(1,6)
print("1.kocka:",dobas)
masodik_osszeg= masodik_osszeg+dobas
dobas = random.randint(1,6)
print("2.kocka:",dobas)
masodik_osszeg= masodik_osszeg+dobas
print("a 2 kocka dobasanak az osszege", masodik_osszeg)

if(masodik_osszeg > elso_osszeg):
    print(f"{masodik_jatekos} nyerte a jatekot")
elif(masodik_osszeg < elso_osszeg):
    print(f"{elso_jatekos} nyerte a jatekot")
else:
    print(f"dontetlen")