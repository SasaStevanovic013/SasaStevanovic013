
razlomak=input("unesi razlomak u oblku teksta: ")
crta=razlomak.find("/")
imenilac=int(razlomak[crta+1:])
brojilac=int(razlomak[0:crta])
rezultat=brojilac/imenilac
print("količnik je: ",rezultat)
