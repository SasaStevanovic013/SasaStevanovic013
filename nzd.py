# određivanje NZD za dva broja
print("PROGRAM ODREĐUJE NZD ZA DVA BROJA! ")

a=float(input("unesi veći br0oj: "))
b=float(input("unesi manji broj: "))

if a<=0 or b<=0:
    print("uneti brojevi moraju biti veći od 0, unesite ponovo brojeve!!!")
else:
    if a%b==0:
        print("Traženi NZD za unete brojeve je: ", b)
    
    else:
       i=a-1
       while i<a:
          if a%i==0 and b%i==0:
              print("NZD je: ", i)
              break
          else:
    
              i=i-1
           

           
           
