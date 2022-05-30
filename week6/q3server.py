import socket
s=socket.socket()
print('Socket Created')
s.bind(('localhost',10323))
s.listen(3)
print('Waiting for connection...')

while True:
    c,addr=s.accept()
    print('Connected to',addr)
    pw=c.recv(1024).decode()
    while (pw=='ping'):
        c.send(bytes('pong','utf-8'))
        pw=c.recv(1024).decode()
    c.close()