# multi_inherit.py


#此示例示意多继承的语法
class Car:
    def run(self, speed):
        print("汽车以", speed, "km/h的速度行驶")

class Plane:
    def fly(self,height):
        print("飞机以海拔", height, "米高度飞行")

class PlaneCar(Car, Plane):
    '''Plane Car 类同时继承汽车类和飞机类'''
    pass

p1 = PlaneCar()
p1.Flyrun(1000)
p1.run(300)