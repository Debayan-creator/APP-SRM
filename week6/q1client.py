import socket
c=socket.socket()
c.connect(('localhost',10321))
print(c.recv(1024).decode())