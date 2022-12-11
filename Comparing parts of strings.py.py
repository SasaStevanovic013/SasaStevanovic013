"""2 Napisati program koji unosi 2 stringa I koji ispituje
da li je podstring koji se nalazi 3 do 5 indeksa( ubrojati I 5. indeks)
isti za oba stringa. Ako je isti ispisati DA a ako nije ispisati NE
. Ako neki od stringova ima manje od 6 karaktera ispisati GRESKA."""

st1=input("Unesi prvi string veći od 5 karaktera; ")
st2=input(" Unesi drugi string veći od 5 karaktera; ")
isecak1=st1[2:6]
isecak2=st2[2:6]
if len(st1)<6 or len(st2)<6:
    print("GREŠKA, string mora da ima 6 ili više karaktera")
elif isecak1==isecak2:
    print("DA")
elif isecak1!=isecak2:
    print("NE")
