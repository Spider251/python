# week.py
#1.
# def isprime(x):
#     for x in range(1,x):
#         isprime = True
#         if x < 2:
#             isprime = False
#         else:
#             for i in range(2,x):
#                 if x % i == 0:
#                     isprime = False
#                     break
#         if isprime:    
#             isprime = True
#     return isprime

# a = isprime(101)
# print(a)

#2.写一个函数prime_m2n(m, n) 返回从m开始,到n结束的范围内的素数(不包含n),返回这些素数的列表,并打印
# def prime_m2n(m,n):
#     L = []
#     for i in range(m,n):
#         isprime = True
#         if i < 2:
#             isprime = False
#         else:
#             for j in range(2,i):
#                 if  i % j == 0:
#                     isprime = False
#                     break
#         if isprime:
#             L.append(i)
#     return L
# a = prime_m2n(1,10)
# print(a)
# 3.写一个函数primes(n)  返回指定范围n以内的素数(不包含n)的全部素数的列表,并打印这些素数
#       L = primes(10)
#       print(L)  # [2,3,5,7]
#       1) 打印100以内的全部素数
#       2) 打印200以内的全部素数的和
#(1)
# def primes(n):
#     L = []
#     for i in range(n):
#         isprime = True
#         if i < 2:
#             isprime = False
#         else:
#             for j in range(2,i):
#                 if i % j == 0:
#                     isprime = False
#         if isprime:
#             L.append(i)
#     return L
# a = primes(101)
# print(a)
# print(sum(a))
# 4.改写之前的学生信息管理程序:
#     改为用两个函数实现
#       1.写函数input_student()来获取学生信息,
#       当输入姓名为空时结束输入.形成字典组成的列表并返回
#       2.写函数print_student(L) 将上述函数得到的打印成为表格显示
#       如:
        # def input_student():
        #     ...
        # def print_student():
        #     ...
        # L = input_student() #获取列表
        # print(L)
        # print_student #打印表格
L = []
def input_student():
    while True:
        a = {}
        name = input("请输入姓名:")
        if not name:
            break
        age = input("请输入年龄:")
        score = input("请输入成绩:")   
        a['name'] = name
        a['age'] = age
        a['score'] = score
        L.append(a)
    return L
input_student()

def print_student(L):
    print('+--------+--------+--------+')
    print('|  name  |   age  |  score |')
    print('+--------+--------+--------+')
    for d in L:
        line = '|' + d['name'].center(8)
        line += '|' + str(d['age']).center(8)
        line += '|' + str(d['score']).center(8)
        line += '|'
        print(line)
    print('+--------+--------+--------+')

print_student(L)



