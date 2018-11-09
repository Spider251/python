# week.py

# 练习：
# 1. 一个球从100米高空落下，每次落地后反弹高度为原高度的一半地，再落下
#     1)写程序算出皮球在第10次落下后反弹多高
#     2)打印10次后求出共经过多少米路程

# 2.分解质因数，输出一个正整数，分解质因数。
# 如输入： 90 则打印： 90 = 2*3*3*5
# (质因数是指最小能被原数整除的素数(不包括1))

#1.
# n = int(input("请输入第几次落地："))
# def high(n):
#     return 100/2**n
# print(high(n))
# def distance(n):
#     s = 100
#     for i in range(0, n):
#         s += (100 / 2 ** i)
#     return s
# print("共结果了%f米路程"%distance(n))







# 2.
a = int(input("请输入一个整数："))
L = []
for i in range(1,101):
    isprime = True
    if i < 2:
        isprime = False
    else:
        for j in range(2,i):
            if i % j == 0:
                isprime = False
                break
    if isprime:
        L.append(i)
d = a
c = []
for i in L: # i是所有的质数
    while True:
        if a % i == 0:
            c.append(i)
            a = a/i
        else:
            break
print(c)
if len(c) == 1:
    print(d,'=',c[0])
elif len(c) == 2:
    print(d,'=',c[0],'x',c[1])
elif len(c) == 3:
    print(d,'=',c[0],'x',c[1],'x',c[2])