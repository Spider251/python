#coding=utf-8
'''
Chatroom
env: python 3.5
socket and fork
'''
# 对于可变容器,改变其内部的数据,外部的数据也会改变

from socket import *
import os,sys

def do_quit(s,user,name):
    msg = "\n%s 退出了聊天室"%name
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[i])
        else:
            s.sendto(msg.encode(),user[i])
    #从字典中删除该用户
    del user[name]

def do_chat(s,user,name,msg):
    msg = "\n%s 说: %s"%(name,msg)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])


def do_login(s,user,name,addr):
    if (name in user) or name == '管理员':
        s.sendto("该用户已存在".encode(),addr)
        return
    s.sendto(b'OK',addr)

    #通知其他如
    msg = '\n欢迎 %s 加入聊天室'%name
    for i in user:
        s.sendto(msg.encode(),user[i])
    #将用户加入user
    user[name] = addr
    print(user)
    


def do_request(s):
    # 存储结构 {'zhangsan':('127.0.0.1',8888)}
    user = {}
    while True:
        msg,addr = s.recvfrom(1024)
        msgList = msg.decode().split(' ')
        #区分请求类别
        if msgList[0] == 'L':
            do_login(s,user,msgList[1],addr)
        elif msgList[0] == 'C':
            #重新组织消息
            msg = ' '.join(msgList[2:])
            do_chat(s,user,msgList[1],msg)
        elif msgList[0] == 'Q':
            do_quit(s,user,msgList[1])


#创建网络连接
def main():
    ADDR = ('0.0.0.0',8888)
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind(ADDR)

    #用于接收各种客户端请求,调用相应的函数处理    
    pid = os.fork()
    if pid < 0:
        print("创建进程失败")
        return 
    elif pid == 0:
        while True:
            msg= input("管理员消息:")
            msg = "C 管理员 " + msg
            s.sendto(msg.encode(),ADDR)
    else:
        do_request(s)
if __name__ == '__main__':
    main()
