# super_init.py

#示例示意用super函数显示调用基类的初始化方法
class Human:
        def __init__(self, n, a):
            self.name = n
            self.age = a
            print("超类被调用")
        def show_info(self):
            print("姓名:",self.name)
            print("年龄:",self.age)

class Student(Human):
    def __init__(self, n, a, s=0):
      super(Student, self).__init__(n, a)
      self.score = s
      print("Student.__init__被调用")
    def show_info(self):
      super().show_info()
      print("成绩:",self.score)

s = Student("小张", 20,100)
s.show_info()