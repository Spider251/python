# Bigwork.py

#第一题
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

#第二题
# a = 99
# for i in range(1,11):
#     i == a
# print(i*a)

#第三题
# a = 0
# for i in range(1,101):
#     a += i
# print(a)

#第四题
# a = 1
# for i in range(1,11):
#     a *= i
# print(a)

#第五题
# a = 2
# for i in range(1,21):
#     if i < 20:
#          a *= 2
# print(a)

#第六题
# b = 0
# for i in range(1,1000,2):
#     b += i
#     print(i)
# print(b)

#第七题
# b = 0
# for i in range(1,1000):
#     if i % 3 == 0 or i % 17 == 0:
#         b += i
# print(b)

#第八题
# b = 0
# for i in range(1,1000):
#     if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#         b += i
# print(b)

#9.
# b = 0
# for i in range(1,100):
#     if i % 3 == 0 or i % 7 == 0 and(i % 3 == 0 and i % 7 == 0):
#         b += 1
# print(b)

#10
# b = 0
# for i in range(1,100):
#     if i % 7 == 0:
#         if i % 2 != 0:
#             b += 1
# print(b)

#11__________________________________________________
# a = []
# for i in range(1,100):
#     a.append(i)
#     b = [i]
#     c = [i+1]
#     print(b,c)
# n = 1
# for i in range(2,101):
#     print(n,"+",n+1,"=",n+i)
#     n += 1

# 12
# n = int(input("请输入一个数字:"))
# for i in range(2,n):
#     if n % i == 0:
#         print("不")
# else:
#     print("是")

# 13
# b = 0
# a = input("请输入:")
# if len(a) < 10:
#     for i in a:
#         b = b + int(i)
#     print(b)

#14
# a = 0
# for i in range(10000,100000):
#     if str(i) == str(i)[::-1]:
#         print(i)
#         a += 1
# print(a)

#15
# b = 0
# a = input("请输入一个数字:")
# if len(a) < 10:
#     b = a[::-1]
# print(int(b))

#16
# for i in range(100,1000):
#     a = i // 100
#     b = i // 10 % 10
#     c = i %10
#     if a**3+b**3+c**3 == i:
#         print(i)

#17
# a = int(input("请输入次数:"))
# m = 100
# c = 0
# for i in range(a):
#     if i < 2:
#         c += 100
#     else:
#         m = m/2
#         c += m
# print(c)

#18
# a = input("请输入一个数:")
# b = 0
# c = 0
# for i in range(1,6):
#     b = a * i
#     d = int(b)
#     c = c + d
#     print(b)
# print(c)

#19
# for a in range(10):
#     for b in range(10):
#         for c in range(10):
#            d = str(a)+str(b)+str(c)
#            e = str(c)+str(b)+str(a)
#            if int(d) + int(e) == 1333:
#                 print(a,b,c)

#20
# import random
# c = []
# for j in range(6):
#     for i in range(6):
#         a = random.randint(48,123)
#         b = chr(a)
#         if b.isdigit() or b.islower() or b.isupper():
#             c.append(b)
#     print(c[j],end="")
# print()

#21
# s = input("请输入一段英文:")
# b = 1
# for i in s:
#     if i == ' ':
#         b += 1
# print(b)

#22
# s  = input("请输入一段数据:")
# c = 0
# for i in s:
#     if i.isdigit():
#         c += int(i)
# print(c)

#23
# s = input("请输入一段数据:")
# b = 0
# c = []
# for i in s:
#     if i not in c:
#         c.append(i)
# for j in c:
#     print(j,s.count(j),end="")

#24
a = int(input("请输入一个数:"))
for i in range(3,a):
    if a % i == 0:
        print("no")
        break
else:
    print("yes")



#25
n = int(input("给一个不大于9的数:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,"x",i,end=" ")
        if j == i:
            break
    print()
    





    
        
    

    


    




