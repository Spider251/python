#  while_embed.py

# 打印 1 ～ 20整数，打印在一行内
#     1 2 3 4 5 6 ...... 20
#     打印以上数据10行





# j = 0
# while j < 10:
#     i = 1
#     while i <= 20:
#         print(i,end=" ")
#         i += 1
#     print()
#     j += 1

# num = int(input("请输入一个数字:"))
# a = 1
# while a <= num:
#     b = 1
#     while b <= num:
#         print(b,end=" ")
#         b += 1
#     print()
#     a += 1
# print()

w = int(input("请输入宽度:"))
#先循环w行
line = 1#line 代表行数
while line <= w:
    # print('1 2 3 4 5')
    i = 1 # 代表正在打印的数
    while i <= w:
        print(i,end=" ")
        i += 1
    print()# 打印一行完成  
    line += 1


