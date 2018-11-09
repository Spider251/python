# myrange.py
# def myrange(start,stop=None,sep=1): 
#     L = []
#     if not stop:
#         for i in range(0,start):
#             L.append(i)
#         return L
#     elif not sep:
#         for i in range(start,stop):
#             L.append(i)
#         return L
#     else:
#         for i in range(start,stop,sep):
#             L.append(i)
#         return L
# L = myrange(4)
# print(L)
# L = myrange(4,6)
# print(L)
# L = myrange(1,10,3)
# print(L)

def myrange(a,b=None,c=1): 
    if b is None:
        start = 0
        stop = a
    else:
        start = a
        stop = b
    if c is None:
        sep = 1
    else:
        sep = c
    return (list(range(start,stop,sep)))

L = myrange(4)
print(L)
L = myrange(4,6)
print(L)
L = myrange(1,10,3)
print(L)
