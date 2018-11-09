'''
电子词典
'''
from socket import *

# http server IP
HOST = '0.0.0.0'
PORT = 8000
ADDR = (HOST,PORT)
my_dict = {}


class HTTPServer(object):
    def __init__(self,address):
        self.address = address
        self.create_socket()
        self.bind(address)
    def create_socket(self):
        self.sockfd = socket()
        # 端口重用
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    def bind(self,address):
        self.ip = address[0]
        self.port = address[1]
        self.sockfd.bind(address)
    def start(self):
        self.sockfd.listen(10)
        print("Listen to port",self.port)
        while True:
            connfd,addr = self.sockfd.accept()
            print("Connect from",addr)
            self.handle(connfd)
    # 处理接收到的请求
    def handle(self,connfd):
        data = self.connfd.recv(4096).decode()
        if data[0] == 'N':
            d[data[1]] == ''
        elif count(data[0]) > 1:
            d[data[0]] == d[1]
        print(d)






if __name__ == '__main__':
    httpfd = HTTPServer(ADDR)
    httpfd.start()  #启动