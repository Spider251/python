# mynumber.py

# 此示例示意 运算符重载
class mynumber:
    def __init__(self, vaule):
        self.data = vaule
    def __repr__(self):
        return "mynum(%d)" % self.data
    def __add__(self,other):
        print("__add__被调用")
        v = self.data + other.data
        obj = mynumber(v)  # 创建一个新对象
        return obj
    def __sub__(self,other):
        return mynumber(self.data - other.data)

n1 = mynumber(100)
n2 = mynumber(200)
print(n1)
print(n2)
# n3 = n1 + n2
n3 = n1.__add__(n2) # 等同于 n1.__add__(n2)
n4 = n1 - n2
print(n1, '-', n2, '=', n4)
print(n1, '+', n2, '=', n3)