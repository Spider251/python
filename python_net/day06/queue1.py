from multiprocessing import Queue
from time import sleep

#创建消息队列
q = Queue(3)

q.put(1)
sleep(0.1)
print(q.empty())
q.put(2)
q.put(3)

print(q.full())
# q.put(4,timeout = 3)
print(q.get()) #先进先出
print(q.qsize()) #取了一条消息，还剩两条消息
q.close()