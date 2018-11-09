from socket import *
from time import sleep,ctime

#创建tcp套接字
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
sockfd.bind(('127.0.0.1',7564))
sockfd.listen(3)

#设置非阻塞状态
# sockfd.setblocking(False)

#设置超时时间
sockfd.settimeout(5)

while True:
    print("Waiting for connect...")
    try:
        connfd,addr = sockfd.accept()
    # 捕获非阻塞异常    
    # except BlockingIOError:
    #     sleep(2)
    # 捕获超时异常
    except timeout:
        print(ctime())
        continue
    else:
        print("Connect from",addr)
        # connfd.setblocking(False)
        data = connfd.recv(1024)
        print("Receicve:",data.decode())
        connfd.close()

sockfd.close()