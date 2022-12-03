import math
lista=[]
clanovi=int(input("Unesi broj clanova liste:  "))
for clan in range(clanovi):
    clan=int(input(" Unesi ceo broj u listu;  "))
    lista.append(clan)

print("Članovi su;  ", lista)
print("Najmanji čllan je:  ",min(lista))
print("Najveći čllan je:  ",max(lista))
