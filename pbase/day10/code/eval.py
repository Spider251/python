# eval.py

# 此示例示意eval函数的参数的用法
x = 100
y = 200
s = 'x + y'
v = eval(s)
print(v)

#假设局部作用域内有 x = 1 ; y = 2
v2 = eval(s, None, {'x':1, 'y':2})  #字典传参
print(v2)
#设置局部作用域内有 y = 2, 全局作用域: x = 10, y = 20
v3 = eval(s, {'x':10, 'y':20},{'y':2})
print(v3)


