# mylist5.py
#此示例示意索引和切片[] 运算符重载方法
class MyList:
    def __init__(self, iterable=()):
        self.data = list(iterable)
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __getitem__(self, i):
        if type(i) is int:
            print("您正在执行切片操作")
        elif type(i) is slice:
            print("您正在执行切片操作")
            print("起始值:%d"%i.start)
            print("终止值:%d"%i.stop)
            print("步长:%d"%i.step)   
        return self.data[i]
    
    
L1 = MyList([1, -2, 3, -4, 5])
x = L1[3:1:-1]
print(x)
