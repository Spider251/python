# # week.py
# 练习:
#   1.看懂下面的程序在做什么
#     def fx(f, x, y):
#         print(f(x, y))
#     fx((lambda a, b: a + b), 100, 200)
#     fx((lambda a, b: a ** b), 3, 4)
#-----------------------------------------------------
#   2.给出一个整数n,写一个函数来计算
#     1 + 2 + 3 + 4 + ... + n的值并返回结果
#     要求用函数来做
#     如:
#         def mysum(n):
#             ...
#         print(mysum(100))  # 5050
#         print(mysum(10))   # 55
#答案:
'''
def mysum(n):
    # b = 0
    # for i in range(1,n+1):
    #     b += i
    # return b
    return sum(range(1, n + 1))
print(mysum(10))
print(mysum(100))
'''
#-----------------------------------------------------
#   3. 给出一个整数n,写一个函数来计算n!(n的阶乘)
#         n! = 1*2*3*4*...*n
#         def myfac(n):
#             ...
#         print(myfac(5)) # 120
#答案:
# def myfac(n):
#     b = 1
#     for i in range(1,n+1):
#         b *= i
#     return b
# print(myfac(5))

#-------------------------------------------------------
#   4.给出一个整数,写一个函数来计算1+2**2+3**3+ ... +n**n的和
#     (n给一个小点的数)
#答案:
# 方法1
# def my(n):
#     b = 0
#     for i in range(1,n+1):
#         b += i**i
#     return b
# print(my(2))
# 方法2
# def f(n):
#     return sum(map(lambda x:x**x, range(1,n + 1)))
# print(f(2))

#-------------------------------------------------------
#   5.写程序打印杨辉三解(只打印6层)
#         1
#        1 1
#       1 2 1
#      1 3 3 1
#     1 4 6 4 1
#   1 5 10 10 5 1
# 方法1

#第一步,制造相应的列表
def get_next_list(L):
    #用给定的一行L,返回下一行
    #如L为:[1, 2, 1] 则返回 [1, 3, 3, 1]
    rl = [1] #最左边的1
    #算中间的数字(循环获取从0开始的索引)
    for i in range(len(L)-1):
        v = L[i] + L[i + 1]
        rl.append(v)

    rl.append(1)#最右边的1
    return rl

#第二步,生成全部的行放到一个整体的列表rl中,并返回
def yh_list(n):#n为行数
    #如果 n为3 最终返回的列表是:
    #[[1][1,1][1,2,1]]
    rl = []
    L = [1]
    while len(rl) < n:
        rl.append(L) # 加入当前行
        L = get_next_list(L) # 计算出下一行准备加入
    return rl

#第三步,把杨辉三解的列表转为字符串列表
#如果给定的列表是[[1][1,1][1,2,1]]
#返回['1','1 1','1 2 1']
def get_yh_string(L):
    rl = []
    for line in L:
        #line = [1, 2, 1] -> s = '1 2 1'
        str_list = [str(x) for x in line]
        #str_list = ['1','2','1']
        s = ' '.join(str_list)
        rl.append(s)
    return rl
#打印杨辉三解
def print_yh_triangle(L):
    # L = ['1', '1 1', '1 2 1', '1 3 3 1', '1 4 6 4 1', '1 5 10 10 5 1']
    # 打印['1','1 1','1 2 1']
    max_len = len(L[-1])
    for s in L:
        print(s.center(max_len))


L = yh_list(10)
SL = get_yh_string(L)
print_yh_triangle(SL)



# print(get_next_list([1]))
# print(get_next_list([1,1]))
# print(get_next_list([1,3,3,1]))
# print(get_next_list([1,4,6,4,1]))
















# 方法2
# def sanjie(n):
#     L = [[1]]
#     for i in range(2,n+1): # 5
#         L.append([1]*i)
#         for j in range(1,i-1):
#             # L[5][1] = L[3][0]+L[3][1]
#             # L[5][2] = L[3][1]+L[3][2]
#             # L[5][3] = L[3][2]+L[3][3]
#             L[i-1][j] = L[i-2][j-1]+L[i-2][j]
#     for i in range(n):
#         print(' '*(n-i),end="")
#         for j in range(0,i+1):
#             c = L[i][j]
#             if c < 10:
#                 c = '% 1d'% c
#             print(c,end=" ")
#             if j == i:
#                 print()       
# sanjie(6)