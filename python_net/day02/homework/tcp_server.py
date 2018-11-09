import socket

#创建套接字
sockfd = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#设置绑定地址
sockfd.bind(('0.0.0.0',1229))

#设置监听
sockfd.listen(5)

print("Waiting for connect...")

#等待处理客户端链接
    
connfd,addr = sockfd.accept()
print('Connect from',addr) #打印客户端地址

#收发消息
f = open('a.jpg','wb')
while True:
    data = connfd.recv(1024) 
    f.write(data)
    if not data :
        break
    n = connfd.send('Receive your msg\n'.encode())
print("Send%dbytes"%n)
f.close()

connfd.close()

#关闭套接字
sockfd.close()
