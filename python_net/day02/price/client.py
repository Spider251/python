from socket import *

sockfd = socket()

addr = ('127.0.0.1',8888)
sockfd.connect(addr) #创建连接



data = open('a.jpg','rb')
while True:
    r = data.read(1024)
    sockfd.send(r)
    if not r:
        break
    r = sockfd.recv(1024)

data.close()
sockfd.close()