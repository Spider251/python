from socket import *

sockfd = socket()   #创建套接字

sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1) #端口重用

sockfd.bind(('0.0.0.0',8888))

sockfd.listen(5)

connfd,addr = sockfd.accept() #等待客户端连接
print("正在连接的客户端地址:",addr)
f = open('/home/tarena/AID1808/python_Net/day02/price/b.jpg','wb')
while True:
    data = connfd.recv(1024)
    f.write(data)
    if not data:
        break
    n = connfd.send("完毕!".encode())
    
f.close()
sockfd.close()

