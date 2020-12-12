import socket

s = socket.socket()
host = socket.gethostname()
port= 8080

s.bind(('',port))
s.listen(5)

print(host)
print("waiting for any incoming connections…")
conn,addr = s.accept()

print(f"[+] Connecting to {addr}")
print(f"[*] Listening as {host}:{port}")

file =open("5.4.txt",'wb')
file_data = conn.recv(1024)
file.write(file_data)
file.close()
print("File has been received successfully.")
s.close()

