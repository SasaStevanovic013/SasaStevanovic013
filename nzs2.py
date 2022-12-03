# određivanje NZS dva broja
print(" PROGRAM PRONALAZI NZS ZA DVA BROJA! ")
a=float(input("unesi veći broj: "))
c=float(input("unesi manji broj: "))
if a<=0 or c<=0:
   print("uneti brojevi moraju biti veći od 0, unesi ponovo brojeve!!!")
else:
    if a%c==0:
        print("NZS je:  ", a)
    else:
        n=a+1
        while n>a:
            if n%a==0 and n%c==0:
                print(" NZS je: ",n)
                break
            else:
              n=n+1
             
    
