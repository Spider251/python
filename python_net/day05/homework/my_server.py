#coding=utf-8
#服务器
from socket import *
import os,sys

def  do_quit(s,user,name):
    msg = '\n%s 退出了聊天室'%name
    for i in user:
        if i == name:
            s.sendto(b'EXIT',user[1])
    #字典中删除该用户
    del user[name]


def do_char(s,user,name,msg):
    mas = '\n %s 说: %s'%(name,msg)
    for i in user:
        if i != name:
            s.sendto(msg.encode(),user[i])

def do_login(s,user,name,addr):
    #如果名字在字典内或名字为管理员,则重新输入
    if (name in user) or name == '管理员':
        s.sendto("该用户已存在".encode(),addr)
        return
    #否则返回OK和客户端呼应
    s.sendto(b'OK',addr)
    #用户进入聊天室通知其他用户
    msg = '\n欢迎 %s 进入聊天室'%name
    #遍历所有用户并发送
    for i in user:
        s.sendto(msg.encode(),user[i])
    #字典加入新用户键值对
    user[name] = addr
    print(user)


def do_requests(s):
    #接受客户端的消息
    #存储结构为{'zhangsan':('127.0.0.1',8888)}
    user = {}
    while True:
        #接收客户端返回的信息,msg为消息,addr为对应的地址
        msg,addr = s.recvfrom(1024)
        #拆分
        msgList = msg.decode().split(' ')
        #区分类别
        if msgList[0] == 'L':
            #判断是否名字重复
            do_login(s,user,msgList[1],addr)
        elif msgList[0] == 'C':
            #用户输入的消息一体化
            msg = ' '.join(msgList[2:])
            do_char(s,user,msgList[1],msg)
        elif msList[0] == 'Q':
            do_quit(s,user,msgList[1])


def main():
    #地址,端口
    ADDR = ('0.0.0.0',8888)
    #创建套接字
    s = socket(AF_INET,SOCK_DGRAM)
    #保证端口的重用性
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
    #把地址丢进去
    s.bind(ADDR)

    #创建新的进程来处理客户端发过来的信息
    pid = os.fork()
    if pid < 0:
        print("创建进程失败")
        return
    elif pid == 0:
        pass
    else:
        do_requests(s)



if __name__ == '__main__':
    main()