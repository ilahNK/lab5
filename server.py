import socket

s = socket.socket()
print("waiting for any incomoming connections…")
host = socket.gethostname()
#host = input(str(“Please enter the host address of the sender:”))
port=8080
#s.connect(('',port))
#print("Connected..")
#filename= input(str("Please enter  a filename for the incoming file:"))
s.bind(('',port))
s.listen(5)

file =open("5.4.txt","wb")
conn,addr = s.accept()
#file.write(file)
file = s.recv(1024)
file.close()
print("file has been received successfully.")

s.close()
