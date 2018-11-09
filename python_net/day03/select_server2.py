# select_server2.py
from socket import *
from select import select 

#创建套接字
s = socket()
#保证可以重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
#设置地址端口
s.bind(('0.0.0.0',8888))
#监听
s.listen(4)

# 添加关注列表
rlist = [s]
wlist = []
xlist = []

while True:
    #IO监控
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        # 如果i是rs,说明i就绪,即客户端发送消息
        if r is s:
            c,addr = r.accept()
            print("Connect from ",addr)
            rlist.append(c)
        # 某个客户端连接套接字就绪,接受消息
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print("收到:",data.decode())
            # r.send("收到消息:".encode())
            wlist.append(r)
    for w in ws:
        w.send("收到消息:".encode())
        wlist.remove(w)
    for x in xs:
        x.close()
        raise
