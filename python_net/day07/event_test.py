from threading import Event

#创建事件对象
e = Event()
e.set() #设置e

e.wait() # 此时阻塞
e.clear() # 清除设置状态
print(e.is_set()) #判断当前状态
print("**************")