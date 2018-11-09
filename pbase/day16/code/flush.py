# flush.py
import time
f = open("myflush.txt",'w')
f.write("aaaaaaaaaaaaaaa")
f.flush() # 强制清空缓冲区
a = 0
while True:
    time.sleep(0.01)
    print(a)
    a += 1
f.close()