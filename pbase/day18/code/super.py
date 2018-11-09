# super.py

# 此示例示意用super函数显示的调用被覆盖的方法
class A:
    def work(self):
        print("A.work被调用")

class B(A):
    def work(self):
        '''此方法会覆盖父类的work方法'''
        print("B.work被调用")
    def mywork(self):
        #调用自己(B类)方法
        self.work()
        #调用父类(A类)方法
        super(B,self).work()
        super().work()
        
    
b = B()
# b.work() # 请问结果是什么?
# A.work(b) # 不推荐
# super(B, b).work() # A.work被调用

b.mywork()