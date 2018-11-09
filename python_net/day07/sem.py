from multiprocessing import Semaphore,Process
from time import sleep
import os

#创建信号量
sem = Semaphore(3)

def fun():
    print("%d 想执行事件"%os.getpid())
    #消耗一个信号量
    sem.acquire()
    print("%d 执行想执行的事件"%os.getpid())
    sleep(3)
    print("%d 事件执行完毕"%os.getpid())

jobs = []
#5个进程每个需要消耗一个信号量,但是初始只有3个信号量
for i in range(5):
    p = Process(target = fun)
    jobs.append(p)
    p.start()

#不够用了,所以又增加了3个量
for i in range(3):
    sleep(5)
    sem.release()#增加一个信号量

for i in jobs:
    i.join()

#输出最后剩余的信号量
print(sem.get_value())