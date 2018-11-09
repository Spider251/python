# price02.py
# 练习
#   写一程序,输入你的生日
#     1) 算出你已经出生了多少天?
#     2) 算出你出生那天是星期几?

import time
# birthday = tuple(int(input("请输入你的生日:")))
a = time.mktime((1997,7,12,0,0,0,0,0,0))
c = time.mktime((2018,9,18,0,0,0,0,0,0))
b = time.localtime(868636800.0)
d = (c-a) /60 /60 /24 /365
print(d)
print(b[6])