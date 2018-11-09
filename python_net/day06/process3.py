# 带参数的进程函数


#示例示意:主进程的结束不会影响到子进程的运行
from multiprocessing import Process
from time import sleep

def worker(sec,name):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

# p = Process(target = worker,args = (2,'肖恩蒙得兹'))
p = Process(target = worker,args = (2,),kwargs = {'name':'肖恩'})
p.start()
p.join(4)
print("***************")