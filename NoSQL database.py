from pymongo import MongoClient # Uvođenje modula u program.
client = MongoClient()# Pravljenje instance klijenta.
db=client.test # Konekcija na test bazu.

while True: # Beskonačna petlja.
    x=input("Da li želite novi unos? Odgovorite sa da ili ne.: ")#Poćetni dijalog i odabir opcija.
    print()# Prazan red.
    
    if x=='da' or x=='Da' or x=='DA': # Izvršenje programa u slučaju odabira potvrdne opcije.
       print() 
       name = input("Unesite ime filma: ")
       year = input("Unesite godinu: ")
       genre=input("Unesite zanr: ") 
       movie = db.movies
       lista = {
       'name': name,
       'year' :year,
       'genre': genre
       }
       movie.insert_one(lista)
       result = movie.find()
       for r in result:
           print("Film: ","Ime filma: ",r['name'],"Godina: ",r['year'],"Žanr: ",r['genre'])
           print()
           
    elif x=='ne' or x=='Ne' or x=='NE':# Prekig izvršenja programa u slučeju odustajanja.
         print()
         print("Program je obustavio unos podataka pošto se odabrali opciju ne!")
         break
        
    else:# Upozorenje kad nije odabrana nijedna od ponuđenih opcija.
        print()
        print ("POGREŠAN UNOS!!! Morate odgovoriti sa da ili ne!")
        print()

   
        


