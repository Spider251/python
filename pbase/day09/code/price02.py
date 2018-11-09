# price02.py
def mysum(*args):
    a = 0
    for i in args:
        a += i
    return a
print(mysum())
print(mysum(1,2,-2.0))