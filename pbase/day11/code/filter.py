# filter.py 过滤器

#判断x是否是奇数,如果是奇数返回True,否则...
# def isodd(x):
#     return x % 2 == 1
# #生成1 - 100 的奇数
# for x in filter(isodd,range(100)):\
#     print(x) 

#生成1~100以内的偶数
# even = [x for x in filter(lambda x:x % 2 == 0,range(1,100))]
# print(even)

def isprimes(x):
    if x < 2:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
primes = [x for x in filter(isprimes,range(100))]
print(primes)