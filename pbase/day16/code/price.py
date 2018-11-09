# price.py

# f = open("data.txt")
# g = f.readline()
# s = str(g).split(" ")
# print("姓名:",s[0],"电话:",s[1],end=" ")
# g = f.readline()
# s = str(g).split(" ")
# print("姓名:",s[0],"电话:",s[1],end=" ")
# g = f.readline()
# s = str(g).split(" ")
# print("姓名:",s[0],"电话:",s[1],end=" ")
# print()

#1. 打开文件
myfile = open("data.txt")
#2. 读取文件
'''
#方法1,每次读取一行,然后进行处理后打印
while True:
    line = myfile.readline()
    if line == '':
        break
    line = line.strip() # 去掉末尾的'\n'
    L = line.split() # 将其拆分为:列表
    print("姓名:",L[0],"电话:",L[1])
'''
'''
#方法2,先读取所有文件数据到内存中,形成列表
lines = myfile.readlines()
for line in lines:
    line = line.strip()
    L = line.split()
    print("姓名:",L[0],"电话:",L[1])
'''
#方法3 用read读取数据到内存中,然后再分行处理
s = myfile.read()
lines = s.split('\n') # 以换行符进行拆分
for line in lines:
    L = line.split()
    print("姓名:",L[0],"电话:",L[1])



#3. 关闭文件
myfile.close()
