import socket

s = socket.socket()
port= 8080
s.connect(('192.168.1.6',port))

print("Connected to Server...Ready to GO!")

filename= input("Let me know the filename. Drop it:")
file =open(filename,"rb")
file_data = file.read(1024)
s.send(file_data)
print("File has been transmitted successfully.")

s.close()

