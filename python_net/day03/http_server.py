from socket import *

#接收request    发送response
def handleClient(connfd):
    request = connfd.recv(4096)
    print(request)
    #将request按行切割
    request_lines = request.splitlines()
    #暂时不做过多解析
    for line in request_lines:
        print(line)
    try:
        #需要在目标文件夹下运行
        f = open('index.html')
    except IOError:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += '\r\n'#空行
        response += '====Sorry not found===='
    else:
        response = "HTTP/1.1 200 OK\r\n"
        response += '\r\n'#空行
        response += f.read()
    finally:
        #无论什么结果都发送给浏览器
        connfd.send(response.encode())
        

#创建套接字
def main():
    #设置流式套接字
    sockfd = socket()
    #端口重用
    sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
    #设置端口
    sockfd.bind(('0.0.0.0',9696))
    #监听
    sockfd.listen(3)
    print("Listen to the port 9696")
    while True:
        connfd,addr = sockfd.accept()
        #处理请求--功能:和客户端交互   所以传入套接字
        handleClient(connfd)
        connfd.close()

if __name__ == '__main__':
    main()