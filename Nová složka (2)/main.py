import random
#1 promena s jmenem
jmeno="David"

#2 promena s prijmeni
prijmeni="Řepišťák"

#3 promene budou vypsane do konzole
print(jmeno)
print(prijmeni)

#4 vstup pro uzivatele kam zada vek
while True:
    vek=input("Jaky je vas vek:")

#9 podminka pro uzivatele kam zada vek
    if vek.isdigit ():
        print("dekuji")
        vek=int(vek)
        break
    else:
        print("zadejte jen ciselnou hodnotu")
#5 v konzili bude vypsana delka jmena i prijmeni
print("delka jmena:", len(jmeno))
print("delka prijmeni:", len(prijmeni))

#6 promena kam se zada hodonota 6
hodnota=6

#7 tohle je cyklus ktery se opakuje 5x
for _ in range(5):
    hodnota +=3

#8 vysledna hodnota po 5 cyklech    
print("vysledna hodnota po 5 cycklech je:", hodnota)

#10 promena do ktere se ulozi nahodne cislo od 1 do 10
nahodnaHodnota=random.randint(1,10) 
print("nahodna hodnota od 1 do 10:",nahodnaHodnota)