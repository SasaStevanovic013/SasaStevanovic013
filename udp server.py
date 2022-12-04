
import socket

server_port = 21060

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_socket.bind(('127.0.0.1', server_port))

print ('[SERVER] Listening at: {}'.format(server_socket.getsockname()))

while True:
    message, address = server_socket.recvfrom(65535)
    message=str(message)

    #Funkcija sorted vraca listu sortiranih karaktera stringa
    lista=sorted(message)
    #Zato moramo spojiti te elemente liste u jedan string
    sortiran="".join(lista)

    print ('[SERVER] The client at {}, originally sent: {}'.format(address, repr(message)))
    server_socket.sendto(bytes(str(sortiran), encoding='utf8'), address)
server_socket.close()

