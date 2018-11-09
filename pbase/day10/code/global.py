# global.py

#此示例示意global语句的用法
'''
v = 100
def f1():
    global v #全局声明
    v = 200
f1()
print('v=',v)
'''
v = 100
def f1(v):
    #报错:
    #SyntaxError: name 'v' is parameter and global
    global v
    print(v)
f1(200)