# 01.py

a = input("请输入第一组数据:")
b = input("请输入第二组数据:")
c = input("请输入第三组数据:")
# print("%20s"%a)
# print("%20s"%b)
# print("%20s"%c)
#思考题：
# 方法1
# max_len = max(len(a),len(b),len(c))
# print(" "*(max_len-len(a))+"%s"% a )
# print(" "*(max_len-len(b))+"%s"% b )
# print(" "*(max_len-len(c))+"%s"% c )

#方法2
max_len = max(len(a),len(b),len(c))
fmt = "%" + str(max_len) + "s"
print(fmt % a)
print(fmt % b)
print(fmt % c)

