import socket

s = socket.socket()
#host = input(str("Please enter the host address of the sender:"))
#host= '192.168.1.6'
port= 8080
s.connect(('192.168.1.6', port))
#print("Connected..")
filename= input(str("Please enter  a filename file:"))
#print(filename)
file= open("5.4.txt",'rb')
file_data = file.read(1024)

#file.write(file_data)
#file.close()
print("file has been received.")

s.close()

