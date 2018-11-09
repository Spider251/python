# try-finally.py


#此示例示意,try-finally语句用法
#以煎蛋,打开天然气,关闭天然气为例

def fry_egg():
    print("打开天然气...")
    try:
        count = int(input("请输入鸡蛋个数:"))
        print("完成煎蛋,共煎了%d个鸡蛋"% count)
    finally:
        print("关闭天然气")
try:
    fry_egg()
except:
    print("煎鸡蛋时,锅翻了,已转移战场")