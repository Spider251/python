# poly.py

# 此示例示意多态中的动态
class Shape:
    '''此类描述图形类的共有属性的方法'''
    def draw(self):
        print("Shape.draw被调用")

class Point(Shape):  # 点类
    def draw(self):
        print("Point.draw被调用")

class Circle(Point): # 圆类
    def draw(self):
        print("Circle.draw被调用")

def my_draw(s):
    s.draw() # 此处显示处多态中的动态

s1 = Circle()
s2 = Point()
my_draw(s2)
my_draw(s1)