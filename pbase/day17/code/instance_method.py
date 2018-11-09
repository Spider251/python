# instance_method.py

#此示例用于示意为Dog类添加吃,睡,玩等实例方法,以实现Dog对象的相应行为

class Dog:
    '''这是一种可爱的小动物'''
    def eat(self, food):
        '''此方法用来描述小狗吃的行为0'''
        print("id为%d的小狗正在吃%s"%(id(self),food))
    def sleep(self, hour):
        print("id为%d的小狗睡了%d小时"%(id(self),hour))
    def play(self, something):
        print("id为%d的小狗正在玩%s"%(id(self),something))
        



dog1 = Dog()
dog1.eat("骨头")
dog1.sleep(1)
dog1.play("球")



dog2 = Dog()
dog2.eat("狗粮")
dog2.sleep(2)
dog2.play("飞盘")
Dog.play(dog2,"feipan")