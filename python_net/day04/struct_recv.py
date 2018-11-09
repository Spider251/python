from socket import *
import struct

s = socket()
s.bind(('127.0.0.1',8888))
s.listen(3)

#确定数据结构
st = struct.Struct('i5sf')

c,addr = s.accept()
data = c.recv(1024)

#解析数据
data = st.unpack(data)
print(data)

c.close()
s.close()