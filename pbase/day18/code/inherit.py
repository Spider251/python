# inherit.py


class  Human:
    '''此类用于描述人类的共性'''
    def say(self, what):
        print("说:",what)
    def walk(self, distance):
        print("走了",distance,"公里")

class Student(Human):
    def study(self,course):
        print("学习:",course)
class Teacher(Student):
    def teach(self,subject):
        print("正在教:",subject)

h1 = Human()
h1.say("天真蓝")
h1.walk(5)
print("--------------")
s1 = Student()
s1.say("学习有点累")
s1.walk(1)
s1.study("Python")
print("--------------")
t1 = Teacher()
t1.teach("继承/派生")
t1.say("终于要放假了")
t1.walk(3)
t1.study("java")