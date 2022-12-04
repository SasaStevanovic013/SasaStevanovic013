import xml.etree.ElementTree as ET

#Definisanje funkcije koja kreira elemente i listu
def MovieXml() :
    # kreiranje osnovnog elementa  
    root= ET.Element("Movies")
    
    # kreiranje elementa roditelja
    new_movie= ET.Element("movie")
    root.append(new_movie)

    # Kreiranje podredjenih elemenata
    data11= ET.SubElement(new_movie, "Ime")
    data11.text = "Zola"
    data12= ET.SubElement(new_movie, "Zanr")
    data12.text = "Komedija"
    data13= ET.SubElement(new_movie, "Godina")
    data13.text = "2021."
    
    new_movie2 = ET.Element("movie")
    root.append (new_movie2)
    
    data21= ET.SubElement(new_movie2, "ime")
    data21.text = "Jahaci pravde"
    data22= ET.SubElement(new_movie2, "Zanr")
    data22.text = "Akcija"
    data23= ET.SubElement(new_movie2, "Godina")
    data23.text = "2021."
       
    new_movie3  = ET.Element("movie")
    root.append(new_movie3)
      
    
    data31= ET.SubElement(new_movie3 , "ime")
    data31.text = "Igra"
    data32= ET.SubElement(new_movie3 , "Zanr")
    data32.text = "Triler"
    data33= ET.SubElement(new_movie3 , "Zanr")
    data33.text = "1997."
    
    #Konverzija u string i ispis
    doc = ET.tostring(root)
    print(doc)

#Poziv funkcije
MovieXml()

    
