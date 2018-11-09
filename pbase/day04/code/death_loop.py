# death_loop.py
# 练习:
#   写一个程序，任意输入一些整数，当输入小于零的数时结束输入，当输入完成后，打印您输入的这些正整数的和
#     如:
#       请输入:1
#       请输入:2
#       请输入:3
#       请输入:4
#       请输入:-1
#     打印:您刚开输入的这些正整数的和是:10
# a = 0
# while True:
#   n = int(input("请输入整数:"))
#   if n < 0:
#     break
#   a = a + n
# print("您输入的是的和:",a)

a = 1
while a < 10:
  b = 1
  while b <= a:
    print(b,"x",a,"=",a*b,end=" ")
    b += 1
  print()
  a += 1
