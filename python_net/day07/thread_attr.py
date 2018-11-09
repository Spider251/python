from threading import Thread,currentThread
import time
def fun():
    time.sleep(3)
    print(currentThread().getName())
    print("线程属性测试")

t = Thread(target = fun,name = 'Tarena')

#设置daemon
t.setDaemon(True)
# t.daemon = True

t.start()

print(t.name)
print(t.getName())
t.setName(name = 'didi')
print(t.name)
#打印线程状态
print(t.is_alive())
# t.join()
print('********主线程结束************')
