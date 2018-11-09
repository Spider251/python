# price02.py
#第一题
# a = int(input("请输入一个季度:\n"))
# if a == 1:
#     print("这个季度有1.2.3月")
# elif a == 2:
#     print("这个季度有4.5.6月")
# elif a == 3:
#     print("这个季度有7，8，9月")
# elif a == 4:
#     print("这个季度有10，11，12月")
# else:
#     print("请正确输入季度")


#第二题

# a = int(input("请输入一个月份：\n"))
# if 0 < a <= 3:
#     print("第一个季度")
# elif a <= 0:
#     print("请正确输入月份")
# elif a < 7:
#     print("第二个季度")
# elif a < 10:
#     print("第三个季度")
# elif a < 13:
#     print("第四个季度")

#此示例示意用if 语句嵌套来实现下面程序的功能

# n = int(input("请输入月份:\n"))
# if 1 <= n <= 12:
#     print("用户输入的是合法的月份")
#     if n <= 3:色
#         print("春天")
#     elif n <= 6:
#         print("夏天")
#     elif n <= 9:
#         print("秋天")
#     elif n <= 12:
#         print("冬天")
# else:
#     print("您输错了")

# a = int(input("请输入一个数字:\n"))
# if a > 0:
#     print(a)
# elif a == 0:
#     print("0")
# else:
#     print(-a)
# a = int(input("请输入一个数字:\n"))
# if a < 0:
#     a = -a
# print(a)

#此示例示意条件表达式的语法和用法
#假设商场促销　满　100　减　20
# money = int(input("请输入商品总金额:\n"))
# pay = money - 20 if money >= 100 else money 
# print("您需要支付:",pay,"元")

#绝对值python三目运算大法
a = int(input("请输入一个数字:\n"))
b = -a if a < 0 else a
print(a,"的绝对值为:",b)







