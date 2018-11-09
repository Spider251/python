# 1. 写程序，实现复制文件功能
#     要求:
#       1. 源文件路径和目标文件路径需手动输入
#       2. 要考虑关闭文件问题
#       3. 要考虑复制超大文件问题
#       4. 要能复制二进制文件
'''
#打开文件
n = input("请输入复制文件的路径")
n1 = input("要复制到的路径")
old = open(n,'rb')
new = open(n1,'ab')
#拷贝
for i in old:
    while True:
        new.write(i)
        new.flush() # 写一条存一条
#关闭文件
old.close()
new.close()
'''
def mycopy(src_file, dst_file):
    #此函数的功能:实现复制文件
    '''src_file:源文件名
       dst_file:目标文件名'''
    try:
        fr = open(src_file,'rb') # fr读文件
        try:
            try:
                fw = open(dst_file,'wb') # fw写文件
                try:
                    while True:
                        data = fr.read(4096)
                        if not data:
                            break
                        fw.write(data)
                except:
                    print("可能U盘被拔出...")
                finally:
                    fw.close()
            except OSError:
                print("打开写文件失败")
                return False
        finally:
            fr.close()
    except OSError:
        print("打开读文件失败")
        return False
    return True
    


s = input("请输入源文件路径名:")
d = input("请输入目标文件路径名:")
if mycopy(s, d):
    print("复制文件成功")
else:
    print("复制文件失败")