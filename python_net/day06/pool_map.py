from multiprocessing import Pool
import time

def fun(n):
    time.sleep(1)
    return n * n

pool = Pool()

#使用map将事件放入进程池
r = pool.map(fun,[1,2,3,4,5,6,7,8,9])
pool.close()
pool.join()
print(r)