# mydeco1.py


#以下函数是装饰器函数,fn用来绑定被装饰函数
def mydeco(fn):
    def fx():
        print('+++++++++++这是fn被调动之前++++++++')
        fn()
        print('-----------这是fn被调动之前--------')
    return fx

@mydeco
def myfunc():
    print('myfunc被调用!')

# 以上@mydeco 等同于在def myfunc之后加了如下语句
# myfunc = mydeco(myfunc)

myfunc()
myfunc()
myfunc()