# mylist.py

class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __len__(self):
        '''此方法必须返回整数'''
        # return len(self.data)
        return self.data.__len__()
    def __abs__(self):
        lst = [abs(x) for x in self.data]
        return MyList(lst)

        # L = []
        # for i in self.data:
        #     L.append(i.__abs__())
        # return MyList(L)

myl = MyList([1, -2, 3, -4])
print(myl)
print("myl 的长度是",len(myl))

myl3 = abs(myl)
print(myl3)   #MyList([1,2,3,4])

# myl2 = MyList()
# print(myl2)