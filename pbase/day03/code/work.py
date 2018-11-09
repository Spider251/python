#  1.输入一个字符串，把输入的字符串中的空格全部去掉(包括字符串中间的空格)
#     1)打印原字符串及长度
#     2)打印处理后的字符串及长度
#   2.写程序，输入三行文字，让这三行文字在一个方框内居中显示
#       如:
#         请输入: hello!
#         请输入: I'm studing python!
#         请输入: I like python!
#       打印如下
#       +--------------------+
#       |       hello!       |
#       |I'm studing python! |
#       |   I like python!   |
#       +--------------------+


# 第一题
# str = input("请输入一组数据:")
# print("原字符为:",str,"字符长度为",len(str))
# str = str.replace(' ','')
# print("转变后的:",str,"字符长度为",len(str))

#第二题
a = input("姓名:")
b = input("性别:")
c = input("家庭住址:")
e = max(len(a),len(b),len(c))
print("+","-"*(e + 2),"+",sep="")
print("| ",a.center(e)," |",sep="")
print("| ",b.center(e)," |",sep="")
print("| ",c.center(e)," |",sep="")
print("+","-"*(e + 2),"+",sep="")




