from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///books.db', echo = True)
meta = MetaData()

while True: # Beskonačna petlja.
    x=input("Da li želite novi unos? Odgovorite sa da ili ne.: ")#Poćetni dijalog i odabir opcija.
    print()# Prazan red.
    if x=='da' or x=='Da' or x=='DA': # Izvršenje programa u slučaju odabira potvrdne opcije.
       print() 
       books = Table(
       'books', meta, 
       Column('id', Integer, primary_key = True), 
       Column('title', String), 
       Column('year', Integer),
       )
       meta.create_all(engine)
       print() 
       book_id = input("Enter book id: ")
       book_name = input("Enter book name: ")
       year = int(input("Enter year: "))
       print() 
       query = books.insert().values(id = book_id, title= book_name, year = year)

       query2 = books.select()

       conn = engine.connect()
       r1 = conn.execute(query)
       result = conn.execute(query2)

       for row in result:
           print("Title: {} | Year: {}".format(row[1], row[2]))
       print() 
       
    elif x=='ne' or x=='Ne' or x=='NE':# Prekig izvršenja programa u slučeju odustajanja.
         print()
         print("Program je obustavio unos podataka pošto se odabrali opciju ne!")
         break
        
    else:# Upozorenje kad nije odabrana nijedna od ponuđenih opcija.
        print()
        print ("POGREŠAN UNOS!!! Morate odgovoriti sa da ili ne!")
        print()

   
        

