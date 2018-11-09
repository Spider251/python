# work.py

# 练习:
#   1. 写程序输入一个三角形的宽和高，打印相应的三角形:
#       如:
#         输入: 3
#       1)
#        *
#        **
#        ***
#       2)
#           *
#          **
#         ***
#       3)
#         ***
#         **
#         *
#       4)***
#          **
#           *
#   2.写一个程序，任意输入一个整数，判断这个数是否为素数(prime)
#     素数(也叫质数), 只能被1和自身整除的正整数
#       如: 2 3 5 7 11 13 17...
#   3.编写程序求下列多项式的值:
#     Sn = 1/1 - 1/3 + 1/5 - 1/7 +....
#     1)求1000000个这样的分数相加的值是多少？
#     2)将上一步的值乘以4打印出来，是多少？
#   4.算出 100 ～ 999之间的水仙花数(NarcissisticNumber)
#     如:
#       153 = 1**3 + 5**3 + 3**3


#第一题:
# i = int(input("请输入一个整数:"))
# for c in range(1,i+1):
#     print('*'*c)
# print()
# for d in range(i,0,-1):
#     print('*'*d)
# print()
# for a in range(1,i+1):
#     print(' '*(i-a),'*'*a)
# print()
# for b in range(i,0,-1):
#     print(' '*(i-b),'*'*b)

#第二题
# 写一个程序，任意输入一个整数，判断这个数是否为素数(prime)
#      素数(也叫质数), 只能被1和自身整除的正整数
#       如: 2 3 5 7 11 13 17...
# num = int(input("请输入一个整数:"))
# for i in range(2,num): 
#     if num % i ==0:
#         print("不是质数")
#         break
# else:
#     print("是质数")


# n = int(input("请输入:"))
# l = []
# for x in range(1,n+1):
#     if n%x == 0:
#         l.append(x)
# if len(l) > 2:
#     print("不是素数")
#     print("它的因素有:",l)
# else:
#     print("是素数")


# 3.编写程序求下列多项式的值:
#     Sn = 1/1 - 1/3 + 1/5 - 1/7 +....
#     1)求1000000个这样的分数相加的值是多少？
#     2)将上一步的值乘以4打印出来，是多少？
# a = 0
# Sn = 0
# for i in range(1,1000000,2):
#     if a % 2 == 0:
#         Sn = Sn + 1/i
#     else:
#         Sn = Sn - 1/i
#     a += 1
# print(Sn)
# print(Sn * 4)

# 4.算出 100 ～ 999之间的水仙花数(NarcissisticNumber)
#     如:
#       153 = 1**3 + 5**3 + 3**3

# for i in range(100,1000):
#     a = i // 100
#     b = i % 10
#     c = i // 10 % 10
#     if i == a**3+b**3+c**3:
#         print(i)

#第一题
# n = int(input("请输入三角形的高"))
# for stars in range(1,n+1):  # 代表*个数
#     print('*'*stars)
# print("--------------------------------------------")
# for stars in range(1,n+1):  # 代表*个数
#     blanks = n - stars  #计算空格个数
#     print(' '*blanks + '*'*stars)
# print("--------------------------------------------")
# for stars in range(n,0,-1):  # 代表*个数
#     print('*'*stars)
# print("--------------------------------------------")
# for stars in range(n,0,-1):  # 代表*个数
#     blanks = n - stars  #计算空格个数
#     print(' '*blanks + '*'*stars)

#第二题
# x = int(input("请输入一个数字:"))
# if x < 2:
#     print("不是素数")
# else:
#     for i in range(2,x):
#         if x % i == 0:
#             print(x,"不是素数")
#             break
#     else:
#         print("是素数")

#第三题
# sn = 0.0
# fenmu = 1
# i = 0   #   控制循环次数
# b = 1   #   控制+ -
# while i < 1000000:
#     r = b * 1/fenmu
#     sn += r
#     b *= -1
#     fenmu += 2
#     i += 1
# print(sn)
# print(sn * 4)

#第四题
# for x in range(100,1000):
#     bai = x // 100
#     shi = x % 100 // 10
#     ge = x % 10
#     if x == bai ** 3 + shi ** 3 + ge ** 3:
#         print(x) 

#第四题列表解法
# for x in range(100,1000):
#     s = str(x) # 转为字符串
#     bai = int(s[0])
#     shi = int(s[1])
#     ge = int(s[2])
#     if x == bai ** 3 + shi ** 3 + ge ** 3:
#         print(x) 

#第四题循环嵌套
for i in range(1,10):
    for j in range(0,10):
        for k in range(0,10):
            if i**3+j ** 3 +k **3  == i*100+j*10+k:
                print(i*100+j*10+k)





