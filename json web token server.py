from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import sqlite3
import jwt
from datetime import datetime, timedelta

# Konekcija sa bazom
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()
 
#Kreiranje tabele
cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
id INT PRIMARY KEY,
name_surname TEXT,
number_of_card INT,
password TEXT,
token TEXT)
""")
 
conn.commit()
 
users = cursor.execute("SELECT * FROM Users")
# Unos podataka u tabelu 
if (len(users.fetchall()) == 0):
    user = [('1', 'Pera_Peric', 1604568433,'dajKes',''), ('2', 'Mita_Mitic',
                 1453856387,'mojeMoje',''), ('3', 'Joca_Jocic', 129763655967,'dajStaDas','')]
    cursor.executemany("INSERT INTO Users VALUES (?, ?, ?, ?,?)", user)
    conn.commit()
#Podaci na serveru    
neto = {'Pera_Peric':134700.00,
        'Mita_Mitic':156070.00,
        'Joca_Jocic':111008.00
}

key='R55hjhgffg4Uio%$&REtzuR4JHk6ljh'
#Kreiranje klase za GET I POST zahteve
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.log_message("Incoming GET request...")
        try:
            name = parse_qs(self.path[2:])['name'][0]
            token = parse_qs(self.path[2:])['token'][0]
            if(self.checkToken(token)==False):
                self.send_response_to_client(200, "Token not valid")
                return
        except:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")
            return

        if name in neto.keys():
            self.send_response_to_client(200, neto[name])
        else:
            self.send_response_to_client(400, 'Name not found')
            self.log_message("Name not found")
            
    def do_POST(self):
        self.log_message('Incoming POST request...')
        data_passed = parse_qs(self.path[2:])
    
        try:
            data = cursor.execute("SELECT %s FROM Users WHERE %s=? and %s=?" %  
                                   ("number_of_card","number_of_card","password"), 
                                   (data_passed['number_of_card'][0], 
                                    data_passed['password'][0]),)
            if (len(data.fetchall()) == 0):
                self.send_response_to_client(400, 'Invalid login')
            else:
                encoded = jwt.encode({'number_of_card': data_passed['number_of_card'][0], 
                                      'exp': datetime.utcnow() +
                                      timedelta(seconds=45)}, key, 
                                      algorithm='HS256')
                
                cursor.execute("UPDATE Users SET %s=? WHERE %s=? and %s=?" % ('token','number_of_card','password'),(encoded,data_passed['number_of_card'][0], data_passed['password'][0]))
                conn.commit()

                self.send_response_to_client(200, 'Token (valid for 45 sec): {}'.format(encoded))


        except KeyError:
            self.send_response_to_client(404, 'Incorrect parameters provided')
            self.log_message("Incorrect parameters provided")


    def send_response_to_client(self, status_code, data):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(str(data).encode())
# Provera tokena
    def checkToken(self, token):
        try:
            payload = jwt.decode(token, key, algorithms='HS256')
        except:
            return False
 
server_address = ('127.0.0.1', 8079)
http_server = HTTPServer(server_address, RequestHandler)
http_server.serve_forever()

