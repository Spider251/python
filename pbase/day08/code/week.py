# 练习:
#   1.写一个函数get_chinese_char_count(s) 函数,此函数实现的功能是给定一个字符串,返回一个字符串中文字符的个数
#     def get_chinese_char_count(s):
#           ...
#     s = input("请输入中英文混合的字符串:")
#     print("您输入的中文字符的个数是:",get_chinese_char_count))
#   2.定义两个函数:
#       sum3(a, b, c) 用于返回三个数的和
#       pow3(x) 用于返回x的三次方(立方)
#     用以上函数计算:
#       1)计算 1的立方+ 2的立方 + 3的立方
#       2)计算 1 + 2 + 3的和的立方
#       即: 1**3 + 2**3 + 3**3 和 (1+2+3)**3

#1.
# def get_chinese_char_count(s):
#     c = 0
#     for i in s:
#         if ord(i) > 127:
#             c += 1
#     return c
# s = input("请输入中英文混合的字符串:")
# print("您输入的中文字符的个数是:",get_chinese_char_count(s))

#2.
def sum3(a, b, c):
    return a + b + c
def pow3(x):
    return x**3

a = sum3(1,2,3)
print(pow3(1)+pow3(2)+pow3(3))
print(pow3(a))

