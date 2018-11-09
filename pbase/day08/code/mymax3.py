# 方法1
# mymax3.py
# def mymax3(a, b, c):
#     return max(a,b,c)
# print(mymax3(100, 300, 200))
# print(mymax3('ABC', '123', 'abc'))

#方法2
# def mymax3(a, b, c):
#     zuida = a
#     if b > zuida:
#         zuida = b
#     if c > zuida:
#         zuida = c
#     return zuida
# print(mymax3(100, 300, 200))
# print(mymax3('ABC', '123', 'abc'))

#方法3
def mymax3(a, b, c):
    z = a if a > b else b
    z = z if z > c else c
    return z
print(mymax3(100, 300, 200))
print(mymax3('ABC', '123', 'abc'))

