from socket import *

s = socket()

#设置端口可以立即重用
#测试用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
print(s.getsockopt(SOL_SOCKET,SO_REUSEADDR))

#套接字地址族
print(s.family)
#套接字类型
print(s.type)
#获取绑定地址
print(s.getsockname())

s.bind(('127.0.0.123',8888))
print(s.getsockname())  

print(s.fileno())

s.listen(3)

c,addr = s.accept()
#客户端连接套接字获取对应客户端地址

print(c.getpeername())


c.recv(1024)

c.close()
s.close()