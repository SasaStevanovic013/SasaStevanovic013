import requests
import jwt

login = input("Do you have a token? (y/n): ")
# Unos i provera korisnika koji imaju token 
if(login == 'y'):
         try:
                
                print("Hello {}".format(token['number_of_card']))

         except:
            print("Something is wrong with token")
            client = input("Unesite korisnika: ")
            r = requests.get("http://127.0.0.1:8079/", params={"name":client,'token': token})
            print("Request method: GET, \nResponse status_code: {}\nResponse data(klijent je): {}".format(r.status_code, r.text))

# Unos podataka za korisnike koji nemaju token
elif(login=='n'):
 
    number_of_card = int(input("Enter your number_of_card : "))
    password = input("Enter your password: ")
    r = requests.post("http://127.0.0.1:8079/", params ={'number_of_card':number_of_card,'password': password})
    print("Request method: POST, \nResponse status_code: {}\n Response data: {}".format(r.status_code, r.text)) 
    print("Copy and save your token!")
else:
    print("Wrong action")

