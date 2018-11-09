# price03.py
# 练习:
#     1. 写一个生成器函数,给出开始值begin,和终止值end,此生成器函数生成begin~end 范围内的全部素数(不包含end)
#       如:
#         def prime(begin, end):
#             ...
#         L = list(prime(10, 20))
#         print(L) #[11, 13, 17, 19]

def prime(begin, end):
    for i in range(begin, end):
        isprime = True
        if begin < 2:
            isprime = False
        else:
            for j in range(2, i):
                if i % j ==0:
                    isprime = False
        if isprime:
            yield i
L = list(prime(2, 50))
print(L)