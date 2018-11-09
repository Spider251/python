# 写一个程序,读入任意行的文字,当输入空行时结束输入
#       打印带有行号的输入结果
#       如:
#         请输入:tarena<回车>
#         请输入:china<回车>
#         请输入:holiday<回车>
#         请输入<回车>
#       输出如下:
#         第1行:tarena
#         第2行:china
#         第3行:holiday
def get_text_input():
    L = []
    while True:
        a = input("请输入任意行文字,当输入空行时结束输入")
        if not a:
            break
        L.append(a)
    for t in enumerate(L,1):
        print('第%d行:%s'%t)    
get_text_input()