import socket
s=socket.socket()
print('Socket Created')
s.bind(('localhost',10322))
s.listen(3)
print('Waiting for connection...')

while True:
    c,addr=s.accept()
    print('Connected to',addr)
    pw=c.recv(1024).decode()
    pw1=pw.upper()
    c.send(bytes(pw1,'utf-8'))
    c.close()