import socket
import sys
import json

file = open('5.4.txt', 'r')
file1 = file.read()
sendData = json.dumps(file1)

clientS = socket.socket()

port = 8080
clientS.connect(('192.168.1.6', port))
while True:
    Input = input('Left Message:')
    clientS.send(str.encode(Input))
    Response = clientS.recv(1024)
    print(Response.decode('utf-8'))

clientS.sendall(bytes(sendData,encoding="utf-8"))

clientS.close()
