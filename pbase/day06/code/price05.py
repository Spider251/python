# price05.py
# L = [(x+y)for x in 'ABC'for y in ['1','2','3']]
# print(L)


#   1.已知有一个字符串:
#     s = '100,200,300,500,800'
#     将其转化为数字组成的列表，列表内部为整数:
#       L = [100，200,300,500,800]
#   2.用列表推导式生成如下列表:
#     L = [1,4,7,10, ... 100]
#   3.用列表推导式生成如下列表(思考题)
#     [[1,2,3], [4,5,6],[7,8,9]]
  
#1.
# s = '100,200,300,500,800'
# L = []
# L1 = s.split(',')
# for x in L1:
#     i = int(x)
#     L.append(i)
# print(L)

#2.
# L = [x for x in range(1,101,3)]
# print(L)

#3.
# L = [[x,x+1,x+2] for x in range(1,8,3)]
# print(L)
# y = [[y for y in range(x,x + 3)]
#         for x in range(1,8,3)]
# print(y)

# L = []
# for x in range(1,8,3):
#     temp = [y for y in range(x,x+3)]
#     L.append(temp)
# print(L)
