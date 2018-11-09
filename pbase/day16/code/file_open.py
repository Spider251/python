# file_open.py

# 此示例示意文件的打开操作

#打开文件
try:
    f = open("mynote.txt") # 打开文件, 用f绑定
    print("成功打开文件")
    #读写文件
    s = f.readline() # 从文件中读取一行文字
    print("您读到的是:",s)
    print("您读到的字符个数是:",len(s))
    #关闭文件
    f.close()
    print("成功关闭文件")
except OSError:
    print("打开文件失败")