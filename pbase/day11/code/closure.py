# closure.py


#定义很多个函数每个函数求 x**y次方,y是可变的
#示意
'''
def pow2(x):
    return x**2
def pow3(x):
    return x**3
def pow99(x):
# ...
def pow99(x):
    return x**99
'''
#以下用闭包来实现-----
# def make_power(y):
#     def fn(x):
#         return x ** y
#     return fn
# pow2 = make_power(2)  # pow2绑定一个闭包
# print('5的平方是:',pow2(5)) # 25


# 用闭包来创建任意的
# f(x) = a*x**2 + b*x + c

def get_fx(a,b,c):
    def fx(x):
        return a*x**2 + b*x + c
    return fx

f123 = get_fx(1, 2, 3)
print(f123(20))
print(f123(50))
