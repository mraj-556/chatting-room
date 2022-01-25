import socket
import json

clientsocket = socket.socket()
clientsocket.bind(('',50006))
clientsocket.connect(('127.0.0.1',60005))  # connects to server's ip address and it's port number
print('client1 connected')

client_socket = clientsocket.getsockname()
print(client_socket[0],client_socket[1])

clientsocket.settimeout(1)


while True:
    try:
        s_msg = clientsocket.recv(1024).decode()
        if s_msg:
            print(str(s_msg))
        
    except:
        msg = input('Enter msg : ')
        msg = [msg,'127.0.0.1',client_socket[1]]
        msg = json.dumps(msg)
        clientsocket.shutdown(socket.SHUT_RDWR)
        clientsocket.close()
        clientsocket = socket.socket()
        clientsocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        clientsocket.connect(('127.0.0.1',60005))
        client_socket = clientsocket.getsockname()
        clientsocket.settimeout(1)
        clientsocket.send(bytes(msg.encode('utf-8')))
