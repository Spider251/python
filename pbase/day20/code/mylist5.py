# mylist5.py
#此示例示意索引和切片[] 运算符重载方法
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __getitem__(self, e):
        for index, j in enumerate(self.data):
            if index == e:
                return j
    def __setitem__(self,i,v):
        print("__setitem__: i=", i, 'v=', v)
        self.data[i] = v
    def __delitem__(self, i):
        del self.data[i]
    
L1 = MyList([1, -2, 3, -4, 5])
# x = L1[2] # x = L1.__getitem__(2)
# print(x)
# L1[1] = 2.2 # L1.__setitem__(1, 2.2)
# print(L1)
del L1[1]
print(L1)
