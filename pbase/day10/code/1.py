L = [1,2]
def f1():
    L = [3, 4, 5]
f1()
print(L)   # [1, 2] 因为f1()只制造两局部变量
def f2():
    global L
    L += [3, 4, 5] # L = L + [3, 4, 5] 一个作用域不能又是全局又是局部
f2()
print(L) # 出错
def f3():
    L[:] = [3, 4, 5]
f3()
print(L)  #[3, 4, 5]
