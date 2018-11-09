#conding=utf-8
#客户端

from socket import * 
import os,sys

#发送消息
def send_msg(s,name,addr):
    while True:
        text = input("\n请开始BB:")
        if text == 'quit':
            msg = 'Q ' + name
            #发送给服务器
            s.sendto(msg.encode(),addr)
            sys.exit("\n退出聊天室")
        #用户发送消息 名字/信息
        msg = 'C %s %s'%(name,text)
        #打包发送给服务器
        s.sendto(msg.encode(),addr)

#接收消息
def recv_msg(s):
    while True:
        data,addr = s.recvfrom(2048)
        #接收服务器发来的退出标志后退出该进程
        if data.decode() == 'EXIT':
            sys.exit(0)
        print(data.decode())



def main():
    #用户登录从命令行输入地址和端口
    if len(sys.argv) < 3:
        print("请输入您的地址,服务器端口号")
        return
    #HOST为用户输入的地址
    HOST = sys.argv[1]
    #PORT端口号
    PORT = int(sys.argv[2])
    ADDR = (HOST,PORT)
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)

    
    while True:
        name = input("请输入用户名:")
        #添加用来服务器判断的标识
        msg = 'L '+name
        #发送给服务器
        s.sendto(msg.encode(),ADDR)
        #等待服务器的回复消息
        data,addr = s.recvfrom(1024)
        if data.decode() == 'OK':
            print("您已加入聊天室")
            break
        else:
            print(data.decode())
     #创建父子进程,一个收消息,一个发消息
    pid = os.fork()
    if pid < 0:
        sys.exit("创建进程失败!!")
    elif pid == 0:
        send_msg(s,name,ADDR)
    else:
        recv_msg(s)

 

if __name__ == '__main__':
    main()