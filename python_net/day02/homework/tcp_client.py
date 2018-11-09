from socket import *

#创建套接字
sockfd = socket()


#发起连接
server_addr = ('127.0.0.1',1229)
sockfd.connect(server_addr)

#发收消息

data = open("1.png",'rb')
while True:
    r = data.read(1024)
    sockfd.send(r)
    if not r:
        break
    r = sockfd.recv(1024)

data.close()
sockfd.close()