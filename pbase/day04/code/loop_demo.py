# loop_demo.py
# num = int(input("请输入一个数字:"))
# #第一行
# print("#" * num)
# i = 1
# while i <= num - 2:
#     print('#' + ' ' * (num-2) + '#')
#     i += 1
# #打印1行
# #最后一行
# if num > 1:
#     print("#" * num)


# 1.写程序，计算:
#     1 + 2 + 3 + 4 + ....... 100 的和
#     并打印结果
# i = 1
# a = 0
# while i <= 100:
#     a = a+i
#     i += 1
# print(a)

#  2.写程序:
#     输入一个开始值用begin绑定
#     输入一个结束值用end绑定
#       计算:
#       从begin开始，到end结束的所有整数的和
#     如:
#       请输入开始值: 1
#       请输入结束值: 10
#     打印:
#        和是: 55

# begin = int(input("开始值:"))
# end = int(input("结束值:"))
# a = 0
# while begin <= end:
#     a = begin + a 
#     begin += 1
# print(a)


begin = int(input("开始值:"))
end = int(input("结束值:"))
a = 0
while begin <= end:
    if a % 5 == 0:
        print()
    print(begin,end=" ")
    begin += 1
    a += 1
print()




