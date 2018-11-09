# binary_fuke_read.py


#此示例示意用二进制模式读取文件中的数据
f = open("mynote.txt",'rb') # 二进制读取数据
b = f.read() #返回字符串
print("读取的长度为:",len(b))
print("内容",b)
s = b.decode()
print("读取的长度为:",len(s))
print("转为字符串后s为:",s)
f.close()