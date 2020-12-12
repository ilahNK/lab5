import socket
import sys
import os
from _thread import *

serverSocket = socket.socket()
host = ''
port = 8080
ThreadCount = 0

try:
    serverSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print(f"[*] Listening as {host}:{port}")
serverSocket.listen(5)

def threaded_Client(connection):
    connection.send(str.encode('READY'))
    while True:
        data = connection.recv(1024)
        reply = "Message from Server:Receiving file" + data.decode('utf-8')
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()


while True:
	Client, addr = serverSocket.accept()
	print("Connected to: " + addr[0] + ':' + str(addr[1]))
	start_new_thread(threaded_Client, (Client, ))
	ThreadCount+=1
	print('Thread Number: ' + str(ThreadCount))

	data = Client.recv(1024)
	data = data.decode("utf-8")
	print ("File Received \n")
	print ("THANK YOU")

serverSocket.close()
