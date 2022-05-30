import socket
c=socket.socket()
c.connect(('localhost',10323))
pw=input('Enter message please: ')
while(pw=='ping'):
    c.send(bytes(pw,'utf-8'))
    print(c.recv(1024).decode())
    pw=input()