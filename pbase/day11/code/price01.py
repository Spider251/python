# price01.py
#求: 1**2 + 2**2 + 3**2 + ... + 9**2的和

#求: 1**3 + 2**3 + 3**3 + ... + 9**3的和

#求: 1**9 + 2**8 + 3**7 + ... + 9**1的和

# 1.
# 方法1
# def f1(x):
#     return x**2
# c = 0
# for i in map(f1,range(1,10)):
#     c += i
# print(c)
# 方法2
# m = map(f1,range(1,10))
# print(sum(m))
# 方法3
# print(sum(map(lambda x:x**2,range(1, 10))))
#2.
# def f2(x):
#     return x**3
# b = 0
# for i in map(f2,range(1,10)):
#     b += i
# print(b)

# 3.
# a = 0
# for i in map(pow,range(1,10),range(9,0,-1)):
#     a += i
# print(a)

print(sum(map(pow,range(1,10),range(9,0,-1))))