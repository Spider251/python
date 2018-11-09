# lambda.py

# def myadd(x, y):
#     return x + y
# myadd = lambda x, y: x+y
myadd = lambda *args : sum(args)

print('20+30=',myadd(20, 30))
print('100+200=',myadd(100, 200))