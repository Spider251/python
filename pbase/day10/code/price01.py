# price01.py
count = 0
def hello(name):
    print('你好',name)
    global count
    count += 1
    return count
hello('Tom')
hello('Jerry')
print('hello函数共被调用%d次'%count)