import socket
c=socket.socket()
c.connect(('localhost',10322))
pw=input('Enter message please: ')
c.send(bytes(pw,'utf-8'))
print(c.recv(1024).decode())