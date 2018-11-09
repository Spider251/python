# price04.py
#第一个return是初始的
#第二个return是递增递减的
def getage(n):
    if n == 1:
        return 10
    return 2 + (getage(n - 1))

print(getage(5))