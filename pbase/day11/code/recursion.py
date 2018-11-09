# recursion.py

#此示例示意递归调用和根据条件结束递归

# `def fx(n):
#     print("递归进入第",n,'层')
#     if n == 996:
#         return
#     fx(n + 1)#进入下一层
#     print("递归退出第",n,"层")

# fx(1)
# print("程序结束")

def myfac(n):
    # 如果n为1则知道 1的阶乘是1,直接返回
    if n == 1:
        return 1
    # 否则,进入递推阶段等待下一个结果后再返回
    return n * myfac(n-1)   
print(myfac(5))  # ??