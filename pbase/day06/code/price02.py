# price02.py

#1
# num1 = int(input("请输入第一个数字:"))
# num2 = int(input("请输入第二个数字:"))
# num3 = int(input("请输入第三个数字:"))
# l = [num1,num2,num3]
# c = sum(l)/len(l)
# print("最大:",max(l),"最小:",min(l),"平均值",c)

#2
L = []
while True:
    print("输入-1退出游戏")
    a = int(input("请输入一些整数"))
    if a == -1:
        print("游戏已退出")
        break
    else:
        L.append(a)
        d = len(L)
        b = max(L)
        c = sum(L)/len(L)
    print("共输入了",d,"个有效数据","输入的最大值为:",b,"输入的平均值为:",c)


