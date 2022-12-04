#Neophodno je kreirati UDP klijenta po uzoru na klijentski fajl iz lekcije UDP protokol (NJ_04). Modifikovati klijentski fajl tako da na ekranu ispisuje vreme koje je
#bilo potrebno od trenutka kada se pošalje poruka do trenutka kada stigne odgovor od servera. Eksperimentisati sa različitim veličinama i tipovima poruka.

import time
import socket
server_port = 21060
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
input_s='Hello,server!'
client_socket.sendto(bytes(input_s, encoding='utf8'), ('127.0.0.1', server_port))
t1=time.time()
input_s_modified, address = client_socket.recvfrom(65535)
t2=time.time()
print('[CLIENT] Response from server {}, is: "{}"'.format(address,str(input_s_modified.decode('utf8'))))
print("Vreme proteklo od slanja poruke do prijema modifikovane poruke je: ",t2-t1)
client_socket.close()



