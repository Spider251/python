# guess_num.py
import random
x = random.randint(0,100)
# print(x)
count = 0 #记录次数
while True:
    y = int(input("请输入一个数字:"))
    if y > x:
        print("您猜大了")
        count += 1
    elif y < x:
        print("您猜小了")
        count += 1
    else:
        print("恭喜你终于特么的猜对了!")
        count += 1
        print('您共猜了',count,'次')
        break
