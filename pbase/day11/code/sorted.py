# sorted.py

#此示例示意sorted函数的用法
L = [5, -2, -4, 0, 3, 1]
L2 = sorted(L) 
print('L2', L2) # L2 [-4, -2, 0, 1, 3, 5]
L3 = sorted(L, reverse=True)
print('L3', L3) # L3 [5, 3, 1, 0, -2, -4]

L4 = sorted(L,key=abs)
print('L4',L4) # L4 [0, 1, -2, 3, -4, 5]

names = ['Tom','Jerry','Spike','Tyke']
L5 = sorted(names,key=len)
print('L5',L5)

L6 = sorted(names)
print('L6',L6)