# Unos clanova niza
#ispis niza
# ispis niza obrnurim redom
#ispis parnih članova niza
#ispis neparnih članova niza
def unos(niz,n):
    for i in range(n):
        niz[i]=int(input("Unesite {0}. broj: ".format(1+i)))
def ispis(niz,n):
    for i in range(0,n):
        print("{0}. broj je: ".format(1+i), niz[i])
def obrnuto(niz,n):
    for i in range(n-1,-1,-1):
        print("{0}. broj je: ".format(1+i), niz[i])
def parnost (a):
    if a%2==0:
        return True
    else:
        return False
def ispis_parnih(niz,n):
    for i in range(0,n):
        if parnost(niz[i]):
            print("Paran broj u nizu je: ", niz[i])
br_el=int(input("Unesite broj elemenata niza: "))
niz_brojeva=[0]*br_el
while 1:
    print("Odaberite: ")
    print("1. za upis elemenata niza ")
    print("2. za ispis elemenata niza ")
    print("3. za obrnuti ispis elemenata niza ")
    print("4. za ispis samo elemenata niza koji su parni ")
    print("5. za kraj rada ")
    izbor=int(input("Vas izbor je? "))
    if izbor==1:
        unos(niz_brojeva,br_el)
    elif izbor==2:
        ispis(niz_brojeva,br_el)
    elif izbor==3:
        obrnuto(niz_brojeva,br_el)
    elif izbor==4:
        ispis_parnih(niz_brojeva,br_el)
    elif izbor==5:
        print("Dovidjenja! ")
        break
