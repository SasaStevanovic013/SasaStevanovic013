# Upis podataka u fajl.
with open("./izrazi.txt","w") as f:
    f.write("4-1")
    f.write("\n")
    f.write("9-3")
    
# Čitanje fajla.
with open("./izrazi.txt","r") as f:
    ulaz1=f.readline()
    ulaz2=f.readline()
    print("Prva linija ",ulaz1) 
    print("Druga linija ",ulaz2)

    print() # Stampanje praznog reda.

    # Razdvajanje stringa kod znaka - .
    br1= ulaz1.split("-")
    br2=ulaz2.split("-")

    # Formiranje liste brojeva.
    list1=list(map(int,br1))
    list2=list(map(int,br2))

    # Racunske operacije nad brojevima u listi.
    rez1=list1[0]-list1[1]
    rez2=list2[0]-list2[1]

    # Ispis rezultata.
    print("Rezultat je: ",list1[0],"-",list1[1],"=",rez1)
    print("Rezultat je: ",list2[0],"-",list2[1],"=",rez2)
    print()# Stampanje praznog reda.

    # Konverzija rezultata u string.
    st_rez1=str(rez1)
    st_rez2=str(rez2)

    # Formiranje liste stringova.
    l1=list(map(str,list1))
    l2=list(map(str,list2))

    # Ubacivanje u listu stringova.
    l1.insert(1,"-")
    l1.insert(4,"=")
    l1.insert(5,st_rez1)


    l2.insert(1,"-")
    l2.insert(4,"=")
    l2.insert(5,st_rez2)

    # Formiranje finalnog stringa
    ll1=(" ".join(l1))
    ll2=(" ".join(l2))
    
    # Upis finalnih stringova u fajl.
with  open("./izlaz.txt","w") as f1:
    f1.write(ll1)
    f1.write("\n")
    f1.write(ll2)
    
# Provera sadrzaja fajla izlaz.txt
with  open("./izlaz.txt","r") as f1:
    ulaz11=f1.readline()
    ulaz22=f1.readline()
    print("Prva linija ",ulaz11) 
    print("Druga linija ",ulaz22)
    


    


    

    

    

    
    
    

                
	
