# # price04.py

# 写程序.输入一个开始的整数值用begin绑定
#     输入一个结束的整数用end绑定
#       将从begin开始到end结束的所有偶数存于列表中，并打印(建议用           列表推导式))
# begin = int(input("开始："))
# end = int(input("结束："))
# a = [i for i in range(begin,end) if i % 2 != 1]
# print(a)

print("输入0退出")
L = []
while True:
    a = int(input("请你输入一大堆的数据:"))
    L.append(a)
    if a == 0:
        break
    else:
        L1 = [i for i in L if i > 0]
        L2 = [i for i in L if i < 0]
print("原列表:",L)
print("正数的列表:",L1)
print("负数的列表:",L2)
