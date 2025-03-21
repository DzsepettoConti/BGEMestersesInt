import random


def dobokocka():
    return random.randint(1,6)

elso_jatekos_dobasok = 0

print("Elso dobasai következnek")

elso_jatekos_dobasok = [dobokocka() for i in range(5)]


print(elso_jatekos_dobasok)

dobas_megvaltoztatas = input("Hanyadik dobást akarja ujradobni: ")

megvaltoztatas_lista = dobas_megvaltoztatas.split(",")

print(megvaltoztatas_lista)

for i in range(len(megvaltoztatas_lista)):
    for j in range(len(elso_jatekos_dobasok)):
        if j+1 == int(megvaltoztatas_lista[i]) :
            regi_szam = elso_jatekos_dobasok[j]
            elso_jatekos_dobasok[j] = dobokocka()
            print (f"{regi_szam} lecserélve: {elso_jatekos_dobasok[j]}")


def dbEgyezik(dobas):
    egyezik = 0
    for i in range(len(dobas)):
        if j in range(len(dobas)):
            if int(dobas[i]) == int(dobas[j]):
                egyezik += 1
    return egyezik

print(elso_jatekos_dobasok)
hanydarabEgyezik = dbEgyezik(elso_jatekos_dobasok)
print(hanydarabEgyezik)



def Eredmeny(dobas):
    match dobas:
        case "Admin":
            print("Adminisztrátor jogosultságok")
        case "Manager":
            print("Manager jogosultságok")
        case "Employee":
            print("Munkavállalói jogosultságok")
        case _:
            print("Ismeretlen szerep")  # Alapértelmezett eset

            
