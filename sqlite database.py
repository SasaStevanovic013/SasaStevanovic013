import sqlite3
conn = sqlite3.connect("TestDataBase.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS Sportisti(
   registarski_broj  INT PRIMARY KEY,
   ime TEXT,
   prezime TEXT,
   datum_rodjenja text,
   visina  FLOAT,
   tezina  float,
   sport TEXT,
   disciplina_pozicija TEXT);
""")
conn.commit()

while True:
    unos=input('Do you want to enter data? Yes/No: ')
    if unos=='Yes':
        reg_broj=int(input("Unesite registarski_broj: "))
        ime=input("Unesite ime: ")
        prezime=input("Unesite prezime: ")
        datum_rodj=input("Unesite datum rodjenja: ")
        visina=float(input("Unesite visinu: "))
        tezina=float(input("Unesite tezinu: "))
        sport=input('Unesite sport: ')
        disciplina_pozicija=input('Unesite disciplinu-poziciju: ')
        sportista = (reg_broj,ime,prezime,datum_rodj,visina,tezina,sport,disciplina_pozicija)
        cursor.execute("INSERT INTO Sportisti VALUES (?, ?, ?, ?, ?, ? ,?,?)", sportista)
        conn.commit()
    
    elif unos=='No':
        break
    
    else:
        print('Pogresan unos. Unesite Yes ili No')

cursor.execute("SELECT * FROM Sportisti;")

sportisti = cursor.fetchall()
reg_broj_sportiste=int(input('Unesite reg broj sportiste kojeg zelite da izbrisete iz baze: '))

obrisan=False
for sportista in sportisti:
    if sportista[0]==reg_broj_sportiste:
        cursor.execute("DELETE from Sportisti where registarski_broj = {};".format(reg_broj_sportiste))
        conn.commit()
        obrisan=True          
        break

if obrisan==True:
    print('Izbrisan je sportista sa registarskim brojem ',reg_broj_sportiste)

else:
    print("U bazi ne postoji sportista sa registarskim brojem ",reg_broj_sportiste)

