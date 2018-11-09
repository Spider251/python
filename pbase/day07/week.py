# week.py
# 1.已知有两个等长的列表
#     list1 = [1001, 1002, 1003, 1004]
#     list2 = ['Toom', 'Jerry', 'Spike', 'Tyke']
#     写程序生成如下字典:
#         {'Tom':1001,'Jerry':1002,'Spike':1003,'Tyke':1004}

# 1.
# list1 = [1001, 1002, 1003, 1004]
# list2 = ['Toom', 'Jerry', 'Spike', 'Tyke']
# d = {list2[i]:list1[i] for i in range(0,len(list1))}
# print(d)

# 2.任意输入多个学生的姓名,年龄,成绩,每个学生信息存入一个字典中,然后再放入列表中(每个学生信息需要手动输入)
#     如:
#         请输入姓名: tarena
#         请输入年龄: 15
#         请输入成绩: 99
#         请输入姓名: name2
#         请输入年龄: 22
#         请输入成绩: 100
#         请输入姓名: <直接回车结束输入>
#     在程序内部生成如下列表:
#     L = [{'name':tarena,'age':15,'score':99},
#             {'name':name2,'age':22,'score':100}]
#     1. 打印出上述列表
#     2. 以下列表的形式打印出上述信息
#         +-----------+-----------+-----------+
#         |    name   |    age    |   score   |
#         +-----------+-----------+-----------+
#         |  tarena   |     15    |    99     |
#         |   name2   |     22    |   100     |
#         +-----------+-----------+-----------+
'''
L = []
while True:
    a = {}
    name = input("请输入姓名:")
    if not name:
        break
    age = input("请输入年龄:")
    score = input("请输入成绩:")   
    a['name'] = name
    a['age'] = age
    a['score'] = score
    L.append(a)   
print(L)
print('+--------+--------+--------+')
print('|  name  |   age  |  score |')
print('+--------+--------+--------+')
len_L = len(L)
for i in range(len_L):
    a = L[i]
    print('|'+a['name'].center(8)+'|'+a['age'].center(8)+'|'+a['score'].center(8)+'|')
print('+--------+--------+--------+')
'''

L = []
while True:
    a = {}
    name = input("请输入姓名:")
    if not name:
        break
    age = input("请输入年龄:")
    score = input("请输入成绩:")   
    a['name'] = name
    a['age'] = age
    a['score'] = score
    L.append(a)
max_len = max(len(name),len(age),len(score))   
print(L)
print('+--------+--------+--------+')
print('|  name  |   age  |  score |')
print('+--------+--------+--------+')
for d in L:
    line = '|' + d['name'].center(8)
    line += '|' + str(d['age']).center(8)
    line += '|' + str(d['score']).center(8)
    line += '|'
    print(line)
# len_L = len(L)
# for i in range(len_L):
#     a = L[i]
#     print('|'+a['name'].center(8)+'|'+a['age'].center(8)+'|'+a['score'].center(8)+'|')
print('+--------+--------+--------+')


    
    

    
