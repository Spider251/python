# price03.py
# 练习:
#     1.输入一个整数代表开始用begin绑定
#       输入一个整数代表结束用end绑定
#       打印 begin ～ end(不包含end) 之间的全部奇数
#     2.求 1～100之间所有不能被2,3,5,7,整除的数
#         1)打印这些数，并打印这些的和
#         2)打印这些数的和

#第一题
# begin = int(input("请输入开始数:"))
# end = int(input("请输入结尾数:"))
# for i in range(begin,end):
#     if i % 2 == 0:
#         continue
#     print(i)

#第二题
a = 0
for i in range(1,101):
    if i % 2 == 0\
    or i % 3 == 0\
    or i % 5 == 0\
    or i % 7 == 0:
        continue
    a += i
    print(i,end=" ")
print("以上数字的和是:",a)
