from select import select
from socket import *

# 创建套接字作为关注的IO
#创建套接字 s
s = socket()
# 保证端口可以重用
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)
# 设置端口和地址
s.bind(('0.0.0.0',8888))
# 监听
s.listen(5)


# 添加到关注列表
# 等待发生的IO对象
rlist = [s]
# 主动处理的IO对象
wlist = []
# 出现异常处理的IO对象
xlist = []


while True:
    # IO监控
    rs,ws,xs = select(rlist,wlist,xlist)
    for r in rs:
        # 如果r is s说明s就绪即有客户端发起链接
        if r is s:
            c,addr = r.accept()
            print("Connect from",addr)
            rlist.append(c)
        # 某个客户端链接套接字就绪，接受消息
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