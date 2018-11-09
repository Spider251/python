# class_variable.py

#此示例示意类变量的定义方法和用法
class Car:
    total_count = 0 #类变量, 用于保存汽车对象的个数
    def __init__(self,info):
        self.info = info
        print("汽车",info,"被创建")
        self.__class__.total_count += 1
    def __del__(self):
        print("汽车",self.info,"被销毁")
        self.__class__.total_count -= 1
        # Car.total_count -= 1

c1 = Car("BYD E6")
c2 = Car("吉利 E7")
print("当前有%d个汽车对象" % Car.total_count)  # 2

print("---------------------------------")
del c2
print("当前有%d个汽车对象"%Car.total_count)   # 1