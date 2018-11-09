from socket import *

#创建套接字
sockfd = socket()


#发起连接
server_addr = ('192.168.213.128',8888)
sockfd.connect(server_addr)

#发收消息
while True:
    data = input(">>")
    if not data:
        break
    sockfd.send(data.encode())
    data = sockfd.recv(1024)
    print("From server",data.decode())
sockfd.close()