# price.py
# 练习:
#     写一个生成器函数 myeven(start, stop) 用来生成从start开始到Stop结束区间内的一系列偶数(不包含stop)
#     如:
#       def myeven(start, stop):
#           ...
#       evens = list(myeven(10, 20))
#       print(evens) # [10, 12, 14, 16, 18]
#       for x in myeven(5, 10):
#           print(x) # 6 8
#       L = [x for in myeven(0, 10)]
#       print(L) # [0, 2, 4, 6, 8]

def myeven(start, stop):
    # while start < stop:
    #     if start % 2 == 0:
    #         yield start
    #         start += 2
    #     else:
    #         start += 1
    #         yield start
    #         start += 2
    for x in range(start,stop):
        if x % 2 == 0:
            yield x
evens = list(myeven(10, 20))
print(evens) # [10, 12, 14, 16, 18]
for x in myeven(5, 10):
    print(x) # 6 8
L = [x for x in myeven(0, 10)]
print(L) # [0, 2, 4, 6, 8]