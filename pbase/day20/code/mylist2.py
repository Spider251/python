class MyList:
    def __init__(self, iterable=()):
        self.data = [x for x in iterable]
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __add__(self,other):
        return MyList(self.data + other.data)
    def __mul__(self,other):
        return MyList(self.data * other)
    def __rmul__(self,lhs):
        return MyList(self.data * lhs)
    def __iadd__(self,rhs):
        self.data.extend(rhs.data)
        return self
    


L1 = MyList(range(1, 4))
print(id(L1))
L2 = MyList([4, 5, 6])
L1 += L2
print(id(L1))
print(L1)