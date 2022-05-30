import socket
s=socket.socket()
print('Socket Created')
s.bind(('localhost',10321))
s.listen(3)
print('Waiting for connection...')

while True:
    c,addr=s.accept()
    print('Connected to',addr)
    c.send(bytes('Ace Attorney Orchestra The Best','utf-8'))
    c.close()