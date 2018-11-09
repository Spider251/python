'''第一遍'''
# class mylist:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#     def __repr__(self):
#         return "mylist(%s)" % self.data
#     def __len__(self):
#         return self.data.__len__()
#     def __abs__(self):
#         lst = [abs(x) for x in self.data]
#         return mylist(lst)

# my1 = mylist([1, -2, 3, -4])
# print(my1)
# print("my1 的长度是",len(my1))
'''第二遍'''
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __len__(self):
#         '''此方法必须返回整数'''
#         return self.data.__len__()
#     def __abs__(self):
#         lst = [abs(x) for x in self.data]
#         return MyList(lst)

# my1 = MyList([1, -2, 3, -4])
# print(my1)
# print("my1 的长度是",len(my1))
'''第三遍'''
# class MyList:
#     def __init__(self, iterable=()):
#         self.data = [x for x in iterable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __len__(self):
#         return self.data.__len__()
#     def __abs__(self):
#         lst = [abs(x) for x in self.data]
#         return MyList(lst)

# my1 = MyList([1, -2, 3, -4])
# print(my1)
# print("my1的长度是", len(my1))
'''第四遍'''
# class MyList:
#     def __init__(self, interable=()):
#         self.data = [x for x in interable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __len__(self):
#         return self.data.__len__()
#     def __abs__(self):
#         lst = [abs(x) for x in self.data]
#         return lst

# my1 = MyList([1,-2,3,-4])
# print(my1)
# print("MyList的长度是",len(my1))
'''第五遍'''
# class MyList:
#     def __init__(self, interable=()):
#         self.data = [x for x in interable]
#     def __repr__(self):
#         return "MyList(%s)"% self.data
#     def __len__(self):
#         return self.data.__len__()
#     def __abs__(self):
#         lst = [abs(x) for x in self.data]
#         return lst
# my1 = MyList([1,-2,3,-4])
# print(my1)
# print("MyList的长度是",len(my1))
'''第六遍'''
# class MyList:
#     def __init__(self, interable=()):
#         self.data = [x for x in interable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __len__(self):
#         return self.data.__len__()
#     def __abs__(self):
#         lst = [abs(x)for x in self.data]
#         return lst

# my1 = MyList([1, -2, 3, -4])
# print(my1)
# print(len(my1))
'''第七遍'''
# class MyList:
#     def __init__(self, interable = ()):
#         self.data = [x for x in interable]
#     def __repr__(self):
#         return "MyList(%s)" % self.data
#     def __len__(self):
#         return self.data.__len__()
#     def __abs__(self):
#         lst = [abs(x)for x in self.data]
#         return lst
# my1 = MyList([1, -2, 3, -4])
# print(my1)
# print(len(my1))
'''第八遍'''
# class MyList:
#     def __init__(self, interable=()):
#         self.data = [x for x in interable]
#     def __repr__(self):
#         return "MyList(%s)"%self.data
#     def __len__(self):
#         return self.data.__len__()
#     def __abs__(self):
#         lst = [abs(x)for x in self.data]
#         return lst
# my1 = MyList([1, -2, 3, -4])
# print(my1)
# print(len(my1))
'''第九遍'''
# class MyList:
#     def __init__(self,interable=()):
#         self.data = [x for x in interable]
#     def __repr__(self):
#         return "MyList(%s)"%self.data
#     def __len__(self):
#         return self.data.__len__()
#     def __abs__(self):
#         lst = [abs(x) for x in self.data]
#         return lst
# my1 = MyList([1, -2, 3, -4])
# print(my1)
# print(len(my1))
'''第十遍'''
class MyList:
    def __init__(self, interable=()):
        self.data = [x for x in interable]
    def __repr__(self):
        return "MyList(%s)" % self.data
    def __len__(self):
        return self.data.__len__()
    def  __abs__(self):
        lst = [abs(x) for x in self.data]
        return lst
my1 = MyList([1, -2, 3, -4])
print(my1)
print(len(my1))