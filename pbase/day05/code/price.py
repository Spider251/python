# price.py

# 3.求 100 以内有哪些数与自身 + 1 的乘积再对11求余结果等于8?
#         x *(x+1) % 11 == 8
#     4.输入一段字符串，判断您输入的字符串中有几个文字符:
#         (注意:中文字符的编码值一定大于127) 

# 第三题
# for x in range(1,101):
#     if x *(x+1) % 11 == 8:
#         print(x,end=" ")

#第四题
s = input("请输入一组数据:")
a = 0
for i in s:
    if ord(i) > 127:
        a += 1
print(a)

