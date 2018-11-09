# named_keyword_args2.py

def f2(a, b, *args, c, d):
    print(a, b)
    print(args)
    print(c, d)

# f2(1, 2, 3, 4, d=200, c=100)
f2(11,22,33,**{'c':11, 'd': 22})