# price.py
# 面向对象综合练习:
#     两个人:
#       1.姓名: 张三, 年龄: 35
#       2.姓名: 李四, 年龄: 8
#     行为:
#       教别人学东西 teach
#       赚钱 work
#       借钱 borrow
#       显示自己的信息 show_info
#     事情:
#       张三 教 李四 学 python
#       李四 教 张三 学 王者荣耀
#       张三 上班赚了 1000元钱
#       李四 向 张三 借了 200 元钱
#     打印信息:
#       35 岁的 张三 有钱 800 元 他学会的技能: 王者荣耀
#       8  岁的 李四 有钱 200 元 他学会的技能: python

class Human:
    def __init__(self,name,age):
        self.name = name # 姓名
        self.age = age # 年龄
        self.money = 0 # 钱数
        self.skill = [] # 技能
    def teach(self,other,skill):
        print(self.name,"教",other.name,skill)
        other.skill.append(skill)
    def work(self,money):
        print(self.name,"上班赚钱",money,"元钱")
        self.money += money   
    def borrow(self,other,borrow):
        print(self.name,"借了",other.name,borrow)
        if other.money > borrow:
            other.money -= borrow
            self.money += borrow
        else:
            print("借钱失败!")
    def show_info(self):
        print(self.age,"岁的"+self.name,"有钱",self.money,"元,他学会的技能是",self.skill[0],)


zhang3 = Human("张三", 35)
li4 = Human('李四',8)
zhang3.teach(li4, "python")
li4.teach(zhang3, "王者荣耀")
zhang3.work(1000)
li4.borrow(zhang3, 200)
zhang3.show_info()
li4.show_info()