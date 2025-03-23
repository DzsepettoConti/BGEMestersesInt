import random

def kockadobas():
    return random.randint(1,6)

def jatekosNevKeres(dbJatekos):
    for i in range(dbJatekos):  
        temp_jatekosnev = input("Adja meg az uj jatekos nevet: ")
        jatekos_Nevek.append(temp_jatekosnev)  
    return jatekos_Nevek  


def kockadobasok(jatekosok):
    for i in range(len(jatekosok)):
        temp_Dobas =[]
        temp_Dobas = [kockadobas() for i in range(5)]
        print(f"{jatekosok[i]} ezeket dobta: {temp_Dobas}")
        vegleges_eredmeny = dobasValtoztatas(jatekosok[i], temp_Dobas )



def dobasValtoztatas(jatekos, dobas):
    cserelendo_szamok = 0
    cserelendo_szamok = input("Melyik számokat akarja lecserélni, adja meg a sorzsámukat(1,2,3,4,5), enter ha semmit: ").split(",")
    if len(cserelendo_szamok) > 0:
        for i in range(len(cserelendo_szamok)):
            print(cserelendo_szamok[i]+ ". cserelendo szam")
            for j in range(len(dobas)):
                if int(cserelendo_szamok[i]) == j+1:
                    dobas[j] = kockadobas()
        print(f"{jatekos} új dobása: {dobas}")
        return dobas
    else:
        print(f"{jatekos} nem cserélt dobasokat, számai: {dobas}")
        return dobas

def parKereses(dobas):
    elozoszam = 0
    parok = 0
    gyakorisag = dobas.values()
    return gyakorisag
        



lista = [1,2,1,2,1]
parKereses(lista)


jatekos_szam = int(input("Hany jatekos fog jatszani?"))

jatekos_Nevek = []

jatekosok = jatekosNevKeres(jatekos_szam)

jatekos_Eredmenyek = []


print(jatekosok)

kockadobasok(jatekosok)



        