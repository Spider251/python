# test_write.py
L = []
def print_infos(L):
    while True: 
        n = input("请输入姓名:")
        if not n:
            break
        a = int(input("请输入年龄"))
        c = input("请输入地址")
        L.append(dict(name=n,age=a,address=c))
    return L
def save_to_file(L):
    try:
        f = open("infos.txt",'w')
        for d in L:
            f.write(d['name'])
            f.write('')
            f.write(str(d['age']))
            f.write(' ')
            f.write(d['address'])
            f.write('\n')
        f.close()
    except OSError:
        print("打开文件失败")
def read_from_file():
    '''返回字典组成的列表'''
    L = []
    try:
        f = open("infos.txt",'r')
        while True:
            line = f.readline()
            if not line:
                break
            line = line.rstrip()  #'\n'
            items = line.split()
            d = dict(name=items[0],
                        age=items[1],
                        add=items[2])
            L.append(d)
        f.close()
        print("读取文件成功")
    except OSError:
        print("打开文件失败")
    return L
#1. 从文件中读取数据,形成字典组成的列表
read_from_file()
#2. 打印列表中的数据
print_infos(L)
save_to_file(L)









'''
#打开文件
f = open("infos.txt",'w')
#写入
f.write("小李,20,北京市朝阳区\n")
f.write("小张,18,上海市浦东新区")
# 关闭
f.close()
'''
# f = open("infos.txt")
# s = f.read()
# lines = s.split("\n")
# for line in lines:
#     L = line.split(",")
#     print("姓名:",L[0],"年龄:",L[1],"地址:",L[2])

# f.close()