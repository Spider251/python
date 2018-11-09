from multiprocessing import Pool
from time import sleep,ctime

def worker(msg):
    sleep(2)
    print(msg)
    return ctime()

#创建进程池
pool = Pool(processes=5)
result = []
#向进程池添加事件
for i in range(10):
    msg = "hello %d"%i
    r = pool.apply_async(func = worker,args = (msg,))
    result.append(r) #存储函数事件对象
    #效率低，依次执行,一个一个干，不争不抢，弟弟先行
    # pool.apply(func = worker,args = (msg,))

#关闭进程池
pool.close()

#回收进程池
pool.join()
for i in result:
    print(i.get()) #可以获取进程事件函数的返回值