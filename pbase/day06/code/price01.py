# price01.py

L = [3, 5]
print(id(L))
L[0:0] = [1,2]
L[3:3] = [4]
L[len(L):] = [6]
L[::] = L[:0:-1] # 新建的列表，重新赋值给L
print(id(L))
print(L)