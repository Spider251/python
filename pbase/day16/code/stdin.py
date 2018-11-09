# stdin.py
import sys

# 从标准输入文件中读取内容
# ctrl + d 输入文件结束符
s = sys.stdin.readline()
print(s) 
print("len(s)=",len(s))


sys.stdin.close() #关闭文件,关闭之后input将不能使用
s = input("请输入:")
print(s)