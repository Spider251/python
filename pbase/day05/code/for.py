# for.py

#此示例示意for 语句的语法和使用

# s = "ABCDE"
# for ch in s:
#     print("ch--->",ch)
# else:
#     print("遍历字符串",s,'结束')

# 任意输入一段字符串
#         1)计算这个字符串的'a'这个字符的个数，并打印出来
#         2)计算出空格的个数，并打印出来
#         (要求:用for语句实现，不允许使用 S.count方法)
#     思考:
#         用while语句能否实现上述功能？

s = input("请输入一段字符串:")
a = 0
b = 0
for i in s:
    if i == 'a':      
        a += 1
    elif i == ' ':      
        b += 1
print("a的个数:",a,"空格的个数:",b)