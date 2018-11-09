# with.py
'''
try:
    # 用with语句实现
    f = open("text.txt","w")
    try:

        s = int(input("请输入整数:"))     #故意制造异常

        f.write("hello")
    finally:
        f.close()
except OSError:
    print("异常已处理")
except:
    print("读取数据失败")
'''


try:
    # 用with语句实现
    # f = open("text.txt","w")
    with open("/home/tarena/AID1808/pbase/day20/code/text.txt","a") as f:
        s = int(input("请输入整数:"))     #故意制造异常
        f.write("%d"%s)
except OSError:
    print("文件打开失败")
except:
    print("写入数据失败")

    
