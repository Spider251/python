# gen_function.py


#此示例示意生成器函数的定义和使用

def myyield():
    '''这是一个生成器函数,此函数用来动态生成2, 3, 5, 7'''
    print("即将生成2")
    yield 2
    yield 3
    yield 5
    yield 7
    
    print("生成器函数调用结束")

gen = myyield()
it = iter(gen) #拿到迭代器时,生成函数不执行
print(next(it)) # 即将生成2, 2
print(next(it))


