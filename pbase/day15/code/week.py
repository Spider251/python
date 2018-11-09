# for i in range(10):
#     for j in range(1,i+1):
#         print(j,"x",i,"=",j*i,end=" ")
#     print()

# def myrange(stop,start=0,step=1):
#     def create(stop,start,step=1):
#         if step < 1:
#             stop,start = start,stop
#             if start > step:
#                 while True:
#                     if start >= stop:
#                         break
#                     else:
#                         yield stop
#                         stop += step
#             elif start < step:
#                 while True:
#                     if start <= stop:
#                         break
#                     else:
#                         yield stop
#                         stop -= step
#         if start == 0:
#             while True:
#                 if start >= stop:
#                     break
#                 else:
#                     yield start
#                     start += step
#         else:
#             stop,start = start,stop
#             while True:
#                 if start >= stop:
#                     break
#                 else:
#                     yield start
#                     start += step
#     for i in create(stop,start,step):
#         print(i)
# myrange(5,1,-1)  #BUG
# myrange(1,5,-1)
# myrange(0,5)

#3. 写一个myfilter生成器函数,功能与filter函数功能完全相同
# L = [x for x in filter(lambda x: x%2, range(10))]
# print(L) #[1, 3, 5, 7, 9]

# def myfilter(fn, iter1):
#     for i in iter1: 
#         if fn(i) == True:
#             yield i

# L = [x for x in myfilter(lambda x: x%2, range(10))]
# print(L) #[1, 3, 5, 7, 9]




# 僵尸解答:
# 2.
# def myxrange(start, stop=None, step=1):
#     if stop is None:
#         stop = start
#         start = 0
#     # 正向生成:
#     if step > 0:
#         while start < stop:
#             yield start
#             start += step
#     elif step < 0:
#         while start > stop:
#             yield start
#             start += step #加上一个负数

# L = [x ** 2 for x in myxrange(1,101,2)]
# print(sum(L))