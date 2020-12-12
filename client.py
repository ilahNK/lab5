import socket
s= socket.socket()
port= 8080
s.connect('192.168.1.6', port)

filename=input(str("Please enter filename:"))
file=  open(filename,'rb')
file_data= s.recv(1024)
conn.send(file_data)
file.close()
print ("file has been received.")

s.close()
