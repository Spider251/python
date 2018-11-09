# file_write.py

#此示例示意写文本文件
#1. 打开文件
f = open("myfile.txt", 'a')
print("打开文件成功")
#2. 写文件
f.write("这是第一行文字\n")
f.write("HIJKLMN")
f.writelines(["aaaaaaaa","bbbbbb","cccccccc"])
print("写文件成功")

#3. 关闭文件
f.close()
print("文件已关闭")