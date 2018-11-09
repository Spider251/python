#coding=utf-8
'''
客户端
'''
from socket import *

frame_ip = '127.0.0.1'
frame_port = 7979
frame_address = (frame_ip,frame_port)

class Application(object):
    def __init__(self):
        self.sockfd = socket()
        self.sockfd.bind(frame_address)
        
    def start(self):
        self.window()
        while True:
            data = input(">>")
            if data not in ['1','2','3']:
                continue
            elif data == '1':
                use_name = input("user_name>>")
                use_name = 'N '+use_name
                self.sockfd.send(use_name.encode())
                password = input("password>>")
                password = use_name+' '+password
                self.sockfd.send(password)
                
            elif data == '2':
                pass
            elif data == '3':
                pass
        # self.choose()
    def window(self):
        print("+"+'-'*27+"+")
        print("+          1. 注册          +")
        print("+          2. 登录          +")
        print("+          3. 退出          +")
        print("+"+'-'*27+"+")
    # def cloose(self):
        




if __name__ == '__main__':
    app = Application()
    app.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    app.start() # 启动