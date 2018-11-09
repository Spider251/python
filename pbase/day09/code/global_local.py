# global_local.py

#此示例示意全局变量和局部变量
a = 100     # a全局变量
b = 200     # b全局变量
def fx(c):  # c是局部变量
    d = 400 # d是局部变量
    print(a, b, c, d)  #优先访问局部变量
    
fx(300)
print('a=',a)
print('a=',b)
