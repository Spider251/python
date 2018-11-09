# mydeco2.py


#此示例用装饰器改变原来函数的调用流程(业务流程)
#银行业务

def privileged_check(fn):
    def fx(n, x):
        print("正在进行权限验证...")
        fn(n,x)
        print("已经发送短信到您手机...")
    return fx

@privileged_check
#以下是郭老师写的程序
def save_money(name, x):
    print(name, '存钱', x, '元')
@privileged_check
def withdraw(name, x):
    print(name, '取钱', x, '元')

#-----以下小张写的程序------
save_money('张云雷',200)
save_money('杨九郎',400)
withdraw('岳云鹏',500)