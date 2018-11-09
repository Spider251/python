import os

filename = "./1.png"
#获取文件大小
size = os.path.getsize(filename)
print(size)

#父子进程共用一个文件对象偏移量会相互影响
#所以f=open(filename,'rb')不能放在外部,需要各自打开文件进行操作
#举个栗子:如果下半部分先执行,上半部分则不执行


#上半部分
def copy1():
    f = open(filename,'rb')
    n = size // 2
    fw = open('a.jpg','wb')
    while True:
      if n < 1024:
        data = f.read(n)
        fw.write(data)
        break
      data = f.read(1024)
      fw.write(data)
      n -= 1024
    f.close()
    fw.close()

#下半部分
def copy2():
    f = open(filename,'rb')
    fw = open('b.jpg','wb')
    f.seek(size//2,0)
    while True:
      data = f.read(1024)
      if not data:
        break
      fw.write(data)
    f.close()
    fw.close()

pid = os.fork()
if pid < 0:
    print("Create process failed")
elif pid == 0:
    copy1()
else:
    copy2()