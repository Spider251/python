# mro.py

# 此示例示意__mro__类属性和用法

class A:
    def go(self):
        print("A")
class B(A):
    def go(self):
        print("B")
        super().go() # C
class C(A):
    def go(self):
        print("C")
        super().go() # A
class D(B, C):
    def go(self):
        print("D")
        super().go()  # B
        for i in D.__mro__:
            print(i)
d = D()
d.go() # D