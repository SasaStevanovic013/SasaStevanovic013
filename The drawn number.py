#Program pita da li pristaješ na bacanje kockice, i vrednosti upisuje u listu
import random
vrednost=[]
pitanje ="da"
pitanje=input(" Da li želite da nastavite igru. Odgovorite sa da ili ne: ")
while  pitanje=="da":
   broj=random.randint(1,6)
   vrednost.append(broj)
   print("izvučeni brojevi su; ",vrednost)
   pitanje=input(" Da li želite da igrate: ")
print("Prijatan dan!")   
