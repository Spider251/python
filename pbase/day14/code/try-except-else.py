# try-except-else.py

#此示例示意try-except 语句的基本语法和用法

def div_apple(n):
    print("现在有%d个苹果,你想分给几个人?" % n)
    s = input("请输入人数:")
    count = int(s) # 可能触发ValueError错误
    result = n / count # ZeroDivisionErro
    print("每个人分了%d个苹果" % result)
try:
    div_apple(10)
except :
    print("有异常发生")
else: # 此子句只有在此try语句内没有发生异常时执行
    print("没有异常发生")
# except ZeroDivisionError:
#     print("把苹果拿回来") 
print("程序正常结束")