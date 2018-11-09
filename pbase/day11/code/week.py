# week.py
# 练习:
#   1.编写程序求 1 ~ 20的阶乘的和
#     即:
#       1! + 2! + 3! + ... + 20!
# def Jc(x):
#     if x == 1:
#         return 1
#     return x * Jc(x-1)
# a = sum(map(Jc,range(1,21)))
# print(a)
#   2.改写之前的学生信息管理系统
#     要求添加四个功能:
#         5) 按学生成绩高-低显示学生信息 |
#         6) 按学生成绩低-高显示学生信息 |
#         7) 按学生年龄高-低显示学生信息 |
#         8) 按学生年龄低-高显示学生信息 |
#   3. 已知有列表:
#   L = [[3,5,8],10,[[13,14],15,18],20]
#   1) 写个函数print_list(lst) 打印出所有的数字,即:
#       print_list(L) #打印 3 5 8 10 13 ...
#   2) 写一个函数sum_list(lst) 返回这个列表中所有数字的和
#       print(sum_list(L)) #126
#   注:
#     type(x) 可以返回一个变量的类型,如:
#       >>> type(20) is int # True
#       >>> type([1, 2, 3]) is list # True

L = [[3,5,8],10,[[13,14],15,18],20]
# def print_list(lst):
#     for i in lst:
#         if type(i) is int: 
#             print(i,end=" ")

#         else:
#             print_list(i)
            
# print_list(L)

a = 0
def sum_list(lst):
    global a
    for i in lst:
        if type(i) is int:
            a += i
        else:
            sum_list(i)
    return a
b = sum_list(L)
print(b)    




    
