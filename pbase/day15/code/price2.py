# price2.py
# 练习:
#     已知有列表:
#       L = [2, 3, 5, 7, 10, 15]
#     1) 写一个生成器函数,让此函数能动态提供数据,数据为原列表的数字的平方+1
#     2) 写一个生成器表达式,让此表达式能动态提供数据,数据依旧为原列表数字的平方+1
#     3) 生成一个列表,此列表内的数据为原列表的数字的平方+1

L = [2, 3, 5, 7, 10, 15]
# def gen(L):
#     for i in L:
#         c = i ** 2 +1
#         yield c
# a = gen(L)
# it = iter(a)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# gen = (x ** 2 +1 for x in L)
# it = iter(gen)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

gen = (x ** 2 +1 for x in L)
l = []
for x in gen:
    l.append(x)
print(l)




