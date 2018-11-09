# weekday01.py# work.py

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
# a = int(input("请输入三角形的高:"))
# for i in range(1,a+1):
#     print("*"*i)
# print()
# for j in range(a,0,-1):
#     print("*"*j)
# print()
# for k in range(1,a+1):
#     print(' '*(a-k),"*"*k)
# print()
# for z in range(a,0,-1):
#     print(' '*(a-z),"*"*z)




#第二题
# 写一个程序，任意输入一个整数，判断这个数是否为素数(prime)
#      素数(也叫质数), 只能被1和自身整除的正整数
#       如: 2 3 5 7 11 13 17...
# a = int(input("请输入一个数:"))
# b = []
# for i in range(1,a+1):
#     if a % i == 0:
#         b.append(a)
# if len(b) > 2:
#     print("不是质数")
# else:
#     print("是质数")

# 3.编写程序求下列多项式的值:
#     Sn = 1/1 - 1/3 + 1/5 - 1/7 +....
#     1)求1000000个这样的分数相加的值是多少？
#     2)将上一步的值乘以4打印出来，是多少？
# c = 0
# Sn = 0
# for i in range(1,1000000*2,2):
#     if c % 2 == 0:
#         Sn += 1/i
#     else:
#         Sn -= 1/i
#     c += 1
# print(Sn)
# print(Sn*4)


# 4.算出 100 ～ 999之间的水仙花数(NarcissisticNumber)
#     如:
#       153 = 1**3 + 5**3 + 3**3
# for i in range(100,1000):
#     bai = i // 100
#     ge = i % 10 
#     shi = i // 10 % 10
#     if bai**3+ge**3+shi**3 == i:
#         print(i)


#扩展题-------菱形
# a = int(input("请输入三角形的高:"))
# for i in range(1,a+1):
#     you = "*"*i
#     print(' '," "*(a-i),"*"*(i-1),you,sep="")
# print("*"*(2*a+1))
# for i in range(a,0,-1):
#     you = "*"*i
#     print(' '," "*(a-i),"*"*(i-1),you,sep="")

#扩展题----圣诞树
# a = int(input("请输入三角形的高:"))
# for i in range(1,a+1):
#     you = "*"*i
#     print(' '," "*(a-i),"*"*(i-1),you,sep="")
# c = a
# for i in range(1,a+1):
#     shugen = "***"
#     print(" "*(a-2),shugen)
            #   a b c
            # a b c 
#输出40个契数 1 1 2 3 5 8 13...
# a = 1
# b = 1
# d = []
# for i in range(1,41):
#     c = a + b 
#     d.append(a)
#     d.append(b)
#     d.append(c)
#     a = c + b
#     b = c + a
# print(d[0:40])

#输出一个字符串，打印处这个字符串出现过的每个字符和他出现过的次数

            
        


    
     
