# price03.py

def min_max(z,*args):
    a = max(z,*args)
    b = min(z,*args)
    return b,a
print(min_max(10,20,30))
x,y = min_max(8,6,4,3,9,2,1)
print("最小值是:",x)
print('最大值是:',y) 
# print(min_max()) #没有实参报错

# def min_max(a,*args):
#     zuixiao = a
#     for x in args:
#         if x < zuixiao:
#             zuixiao = x
#     zuida = a
#     for x in args:
#         if x > zuida:
#             zuida = x
#     return zuixiao,zuida 

# print(min_max(10,20,30))
# x,y = min_max(8,6,4,3,9,2,1)
# print("最小值是:",x)
# print('最大值是:',y)
# print(min_max())