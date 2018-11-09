# instance_attribute.py

#此示例示意创建和使用实例属性

class Dog:
    '''这是一种可爱的小动物'''
    def eat(self, food):
        '小狗吃东西的行为'
        print(self.color,"的",self.kinds,'正在吃',food)
        # 以下让当前的小狗自己记住吃的是什么
        self.last_food = food
    def show_info(self):
        print(self.color,"的",self.kinds,"上次吃的是:",self.last_food)

dog1 = Dog()
dog1.kinds = "哈士奇"   # 创建属性
dog1.color = "黑白相间"     # 创建 属性color
dog1.color = "雪白"     # 修改属性color
print(dog1.color,"的",dog1.kinds)
dog1.eat("狗头")        

dog2 = Dog()
dog2.kinds = "藏獒"
dog2.color = "棕色"
dog2.eat("狗粮")


dog1.show_info()
dog2.show_info()