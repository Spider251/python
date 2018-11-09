
# 练习：
#   1. 编写函数 fun，其功能是计算下列多项式的和
#       f(n) = 1 + 1/1！ + 1/2！ + 1/3！ + ... +1/n！
#       当n等于20时，此函数的值
#   2. 写一个程序，以电子时钟格式显示时间：
#       格式为：
#           HH:MM:SS  如： 15：58：26
#   3. 编写一个闹钟程序，启动时设置定时时间，到时间后打印一句“时间到！”，然后退出程序

#1.
'''
import math
def fun(n):
    s = 0
    a = 1
    for i in range(n+1):
        s += 1/math.factorial(i)
    print(s)
fun(20)
#方法2
def f(n):
    s = sum(map(lambda x:1 / math.factorial(x),
                    range(n + 1)))
    return s
print(f(20))
'''
# 2.
# import time
# a = int(input("开始请按1："))
# if a == 1:
#     while True:
#         a = time.localtime() 
#         print("%02d:%02d:%02d"%(a[3],a[4],a[5]),end="\r")
#         time.sleep(1)

#3.编写一个闹钟程序，启动时设置定时时间，到时间后打印一句“时间到！”，然后退出程序
# import time
# b = input("请输入停止时间：")
# while True:
#     a = time.localtime() 
#     c = a[3],':',a[4],':',a[5]
#     print(c,end="\r")
#     if int(b[0:2]) == a[3] and int(b[2:4]) == a[4] and int(b[4:6]) == a[5]:
#         print("时间到勒！！！")
#         break
#     else:
#         time.sleep(1)


#离停止时间的间隔S
# import time
# b = input("请输入停止时间：")
# while True:
#     a = time.localtime() 
#     c = a[3],':',a[4],':',a[5]
#     c_1 = a[3]*3600+a[4]*60+a[5]
#     d = int(b[0:2])*3600+int(b[2:4])*60+int(b[4:6])
#     # print(c,end="\r")
#     print("还差",d-c_1,"S",end="\r")
#     if int(b[0:2]) == a[3] and int(b[2:4]) == a[4] and int(b[4:6]) == a[5]:
#         print("时间到勒！！！")
#         break
#     else:
#         time.sleep(1)

import time
def alarm(h,m): #h小时,m分钟
    print("设置时间为:%02d:%02d"%(h,m))
    while True:
        #得到当前时间的小时和分钟:
        #t = time.localtimne()[3:5]
        t = time.localtime()
        t2 = t[3:5]
        if t2 == (h, m): #判断时间
            print()
            print("时间到!")
            break
        #显示时间,睡一秒
        print("%02d:%02d:%02d" % (t[3],t[4],t[5]),end="\r")
        time.sleep(1)

hour = int(input("请输入小时:"))     
minute = int(input("请输入分钟:"))
alarm(hour,minute)