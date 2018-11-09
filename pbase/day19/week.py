#  2. 自己写一个MyList类,实现重写len,str,让MyList类型的对象变为可迭代对象
# 3. 写一个类,Fibonacci实现迭代器协议,此类的对象可以作为可迭代对象生成相应的斐波那契数
#         1 1 2 3 5 8 13 ......
#         如:
#           class Fibonacci:
#               def __init__(self, n):
#                   ...
#               ....
#         实现如下操作:
#           for x in Fibonacci(5)
#               print(x) # 1 1 2 3 5
#           L = [x for x in Fibonacci(50)]
#           print(L)
#           print(sum(Fibonacci(100)))

class Fibonacci:
    def __init__(self, n):
        self.L = [1,1]
        self.count = n  #记录要生成的数据的个数
        if n == 1:
            self.L == [1]
        elif n == 2:
            self.L == [1,1]
        for i in range(self.count):
            self.L.append(self.L[-1] + self.L[-2])
    def __iter__(self):
        return MyIter(self.L) #return 迭代器
    
class MyIter:
    '''迭代器'''
    def __init__(self, L):
        #可迭代元素
        self.L = L
        #迭代器的起始位置
        self.index = 0
    def __next__(self):
        '''此方法用于可迭代协议'''
        if self.index >= len(self.L)-2:
            raise StopIteration
        #拿到当前下标的列表值
        d = self.L[self.index]
        self.index += 1
        return d
    
for x in Fibonacci(5):
    print(x) # 1 1 2 3 5
L = [x for x in Fibonacci(50)]
print(L)
print(sum(Fibonacci(100)))