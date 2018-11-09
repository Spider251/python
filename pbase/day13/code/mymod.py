#此示例示意自定义模块 mymod及导入方法

'''
这是我的一个自定义模块

这是一个模块的文档的描述部分
此模块有两个函数和两条数据
...
'''
def mysum(n):
    a = 0
    for i in range(1,n+1):
        a += i
    print('自做和模块：计算1+2+3+...+%d'%n,'的和为：',a)

def myfac(n):
    print('正在计算%d!..' % n)

name1 = 'Audi'
name2 = 'Tesla'
if __name__ == '__main__':
    print('在mymod.py模块内的__name__属性值为:')
    print(__name__)

    print('mymod模块被加载')