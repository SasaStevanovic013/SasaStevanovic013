import threading # uvoz modula
class Kocka: # definisanje klase sa poljima i metodama
    def  __init__(self,a):
        self.a=a
    def zapremina(self):
         print("Zapremina kocke je V=",self.a*self.a*self.a,"cm3")

    def obim(self):
        print("Zbir svih ivica kocke je:",12*self.a,"cm")
        
a=float(input("Unesi ivicu kocke u centimetrima: "))# unos ivice kocke
print() # prazan red

kocka=Kocka(a) #kreiranje objekta

#kreiranje niti
if __name__ == "__main__":
    k1=threading.Thread(target=kocka.obim())
    k2=threading.Thread(target=kocka.zapremina())
    
# startovanje niti   
k1.start()
k2.start()

#pauziranje glavnog programa dok se ne izvrše niti  
k1.join()
k2.join()

print() # prazan red
print("Tražena izračunavanja su izvršena!")

            
		
		 
