import multiprocessing as mp
from time import sleep

a = 1

#编写进程函数
def fun():
    sleep(3)
    global a
    print('儿子',a)
    a = 1000
    print("子进程事件")

#创建进程对象
p = mp.Process(target=fun)

#启动进程
p.start()
 
sleep(2)
print("父进程事件")
#回收进程
p.join()

print('爸爸',a)