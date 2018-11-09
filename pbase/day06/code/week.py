# week.py
# 1. 有一些数存于列表中，如:
#     L = [1,3,2,1,6,4,2, ... 98,82]
#     1)将列表L中出现的数字存入到另一个列表L2中
#       要求:
#         重复出现多次的数字只在L2中保留一份(去重)
#     2)将列表中出现两次的数字存于列表L3中，在L3中只保留一份
# 2.计算出100以内的全部素数，将这些素数存于列表中，然后打印出列表中的这些素数
# 3.生成前40 个斐波那契数(Fibonacci)数列中的数
#       1 1 2 3 5 8 13 21
#     要求: 将这些数保存于列表中，打印这些数

# 1.
# L = [1,2,3,1,1,5,45,2,5,4,1,32,65,2,2,3,58,6132]
# L2 = []
# L3 = []
# for i in L:
#     if i not in L2:
#         L2.append(i)
#     else:
#         if L.count(i) == 2:
#             L3.append(i) 
# print("重复出现的数:",L2)
# print("出现2次的数:",L3)


#2.计算出100以内的全部素数，将这些素数存于列表中，然后打印出列表中的这些素数
# l = []
# c = []
# for i in range(1,100):
#     for j in range(1,i+1):
#         if i % j == 0:
#             c.append(i)
#         else:
#             pass   
# for k in range(1,100):
#     if c.count(k) <= 2:   
#         l.append(k)  
# print(l)
'''
先遍历1~100之间的数,如果这个数是素数,那么就加入到一个列表中
'''
'''
L = []  #此容器准备加入素数
for x in range(1,101):
    #如果x是素数,则把x加入到L中,否则跳过
    isprime = True #先假设x是素数
    #如果x不是素数,就把isprime置为False
    if x < 2:
        isprime = False
    else:
        for i in range(2, x):
            if x % i == 0:#整除就不是素数
                isprime = False
                break

    if isprime:     # 一定为素数
        L.append(x)
print(L)
'''

#3.生成前40 个斐波那契数(Fibonacci)数列中的数
#       1 1 2 3 5 8 13 21
#     要求: 将这些数保存于列表中，打印这些数
# l = [1,1]
# for i in range(0,38):
#     a = l[i]
#     b = l[i+1]
#     c = a + b
#     l.append(c)
# print(l)

'''
L = []  # 空列表,准备放入算出来的斐波那契数
a = 0 # a 代表当前一个数的前一个数
b = 1 # b 代表当前的斐波那契数
while len(L) < 40: 
    # 当列表长度不够40就算出一个数,加入到L中
    # 每次循环算处一个数,加入到列表L中
    L.append(b) # 已经有的数放入列表
    c = a + b #求出下一个斐波那契数
    a = b 
    b = c
print(L)


L = []  # 空列表,准备放入算出来的斐波那契数
a = 0 # a 代表当前一个数的前一个数
b = 1 # b 代表当前的斐波那契数
while len(L) < 40: 
    # 当列表长度不够40就算出一个数,加入到L中
    # 每次循环算处一个数,加入到列表L中
    L.append(b) # 已经有的数放入列表
    a, b = b, a + b
print(L)
'''

#方法3
L = [1, 1]
while len(L) < 40:
    L.append(L[-1] + L[-2])
print(L)
    
