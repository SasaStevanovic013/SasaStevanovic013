"""Napisati program koji učitava cele brojeve
I unosi ih u listu sve dok se ne unese 0.
Napraviti string od elemenata liste tako da se
između svakog broja nalazi karakter *."""

lista=[]
while True:
    br=int(input(" Unesi jedan ceo broj: "))
    if br !=0:
       lista.append(br)
       string=str(lista)
       newstr1=string.split(",")
       newstr2=("*".join(newstr1))

    else:
        print(newstr2)
        break
        
    

    
