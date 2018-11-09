# input_numbers.py
def input_numbers():
    L = []
    while True:
        a = int(input("请输入正整数(负数结束):"))
        if a < 0:
            break
        L.append(a)
    return L
L = input_numbers()
print(L)
print('用户输入的最大数是',max(L))
print('用户输入的最小数是',min(L))
print('用户输入的数的和是',sum(L))
