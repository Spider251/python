# override.py

# 此示例示意覆盖的语法
class A:
    def work(self):
        print("A.work被调用")

class B(A):
    def work(self):
        '''此方法会覆盖父类的work方法'''
        print("B.work被调用")
    
b = B()
b.work() # 请问结果是什么?

a = A()
a.work() # 请问结果是什么?