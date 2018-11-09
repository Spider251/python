from socketserver import *

#服务器类型
class Server(ForkingMixIn,TCPServer):
# class Server(ThreadingMixIn,TCPServer):
    pass

#处理具体请求
class Handler(StreamRequestHandler):
    #具体处理方法
    def handle(self):
        print("Connect from",self.client_address)
        while True:
            #self.request 就是accept返回的客户端连接套接字
            data = self.request.recv(1024)
            if not data:
                break
            print(data.decode())
            self.request.send(b'Receive')#Receive 翻译:收到了

if __name__ == '__main__':
    server_addr = ('0.0.0.0',8888)
    
    #创建服务器
    server = Server(server_addr,Handler)
    server.serve_forever() #启动服务器