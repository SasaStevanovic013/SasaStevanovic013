""" Zahtev zadatka: Napraviti fajl brojevi.txt koji izgleda ovako:
12,434,16784,4

U fajl cifre.txt ispisati brojeve čija je suma cifara paran broj.
Brojeve ispisati jedan pored drugog između kojih treba da se nalazi razmak."""

# drugi deo zadatka
# upis u fajl brojeva čiji je zbir cifara paran broj
with open("./brojevi.txt","r") as br: # čitanje podataka iz fajla
    podatak= br.read()
    
with open("./cifre.txt","w") as cifre:#otvaranje fajla za upis podataka
    podaci= podatak.split(",")#razdvajanje stringa brojeva kod zareza
    lista=list(map(int,podaci))
    
    for i in lista:
        a=i%10
        b=i//10
        a1=b%10
        b1=b//10
        a2=b1%10
        b2=b1//10
        a3=b2%10
        b3=b2//10
        
    s=a+a1+a2+a3+b3 
    if s%2==0:
      print(i," ",end=" ")
      cifre.write(str(i))            
                      
