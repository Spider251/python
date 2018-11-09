# myinteger.py

#此示例示意用生成器函数创建生成从0开始到n结束的一系列整数(不包含n)
def myinteger(n): # integer(整数)
    i = 0 # 设置初始值为0
    while i < n:
        yield i # 生成i给next(it) 调用
        i += 1 # 为生成下一个数据做准备
get = myinteger(10)
it = iter(get)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print("---------------------------------------------------")

for x in myinteger(5):
    print(x)