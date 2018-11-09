# context.py
# 此示例示意自定义用 with 管理的对象


#创建类:环境管理器
class A:
    '''此类的对象将可用于with语句中'''
    def __enter__(self):
        print("已经进入到了with语句的内部")
        return self # 把自己返回 由as 绑定
    def __exit__(self, exc_t, exc_v, exc_tb):
        '''exc_t用来绑定异常类型
            exc_v用来绑定异常对象
            exc_tb用来绑定追踪对象
            在没有异常时,三个形参都绑定None'''
        if exc_t is None:
            print("已离开with语句")
        else:
            print("是在出现异常时走异常流程离开的with语句")


with A() as a:
    print("这是with语句内部的print语句")
    int(input("请输入整数:"))
