import socket
import tkinter as tk
import time


                #########################  socket creation and connection  ##########################

server = socket.socket()

print('socket created')

server.bind(('127.0.0.1',60005))      # to bind the socket to a port number for the server
server.listen(3)     # can serve to maximum 3 users at a time buffer
print('waiting for connection')

users_list = []

while True:
    try:
        client_socket , client_address = server.accept()
        server.settimeout(1)
        if client_address[0] not in users_list:
            users_list.append(client_address[0])
            msg = 'Hey I am server'
            client_socket.send(bytes(msg.encode('utf-8')))
            print(client_address,users_list)
    except:
        client_socket.settimeout(1)
        try:
            c_msg = client_socket.recv(1024).decode()
            if c_msg:
                print('c msg :',c_msg)
        except:
            pass
