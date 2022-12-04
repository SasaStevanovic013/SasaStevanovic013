string="3,9,13,4,42"#ulaz
nova=string.split(',')# Razdvajanje elemenata stringa kod zareza
lista=list(nova)# formiranje liste od stringova
""" Prebacivanje tipa podataka u celobrojnu vrednost broja,
izračunavanje kvadrata broja i ispis rezultata u obliku liste"""
lista2=list(map(lambda x:int(x)*int(x),lista))
list_str = list( map(str,lista2))#Konverzija liste brojeva u  listu stringova  
list_str2=(",".join(list_str))#Ubacivanje zareza između članova liste
for i in range(len(list_str2)): 
    print("{}".format(list_str2[i]), end = '')#Konverzija liste stringova u string i ispis stringa,izlaz
print()#Novi red
print(type(list_str2))#Provera tipa podataka izlaza

  


     
  

    
