from greenlet import greenlet

def test1():
    print(12)
    gr2.switch()
    print(34)

def test2():
    print(56)
    print(78)

#将两个函数变为协程
gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch()
gr1.switch()

