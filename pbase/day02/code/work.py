#1.北京出租车计价器
# a = int(input("请输入公里数:"))
# if a <= 3:
#     print("收费:13元")
# elif 15 >= a > 3:
#     print("收费:",13+2.3*(a-3),"元")
#     print("您需要支付:",round(13+2.3*(a-3)),'元')
# elif a > 15:
#     print("收费:",13 + 2.3*(a - 3) + 2.3 * 0.5 * (a-15),'元')
#     print("您需要支付:",round(13 + 2.3*(a - 3) + 2.3 * 0.5 * (a-15)),'元')

#第二题（1）
# a = int(input("请输入语文分数:"))
# b = int(input("请输入数学分数:"))
# c = int(input("请输入英语分数:"))
# d = max(a,b,c)
# e = min(a,b,c)
# f = (a+b+c)/3
# print(d,e,f)

# a = int(input("请输入语文分数:"))
# b = int(input("请输入数学分数:"))
# c = int(input("请输入英语分数:"))
# （4）
# if a > b:
#     if a > c:
#         zuida = a
#     else:
#         zuida = c
# else:
#     if b > c :
#         zuida = b
#     else:
#         zuida = c
# print("最大的值为:",zuida)
    
# （5）
# zuida = a
# if b > zuida:
#     zuida = b
# if c > zuida:
#     zuida = c
# print(zuida)





# （2）
# if a >= b:
#     a,b = b,a
# if c >= a:
#     c,b = b,c
# if a >= c:
#     a,c = c,a
# print("max",b,"min",a)







# （3）
# a = int(input("请输入语文分数:"))
# b = int(input("请输入数学分数:"))
# c = int(input("请输入英语分数:"))
# if a > b and a > c and b > c:
#     print("最大值为:",a,"最小值为",c)
# elif a > b and a > c and b < c:
#     print("最大值为:",a,"最小值为",b)
# elif a < b and a < c and b < c:
#     print("最大值为:",c,"最小值为",a)
# elif a < b and a < c and b > c:
#     print("最大值为:",b,"最小值为",a)
# elif a > b and a < c and b < c:
#     print("最大值为:",c,"最小值为",b)
# elif a < b and a > c and b > c:
#     print("最大值为:",b,"最小值为",c)
# print("平均值为:",(a+b+c)/3)





#第三题
# a = int(input("请输入一个年份:"))
# if a % 100 != 0 and a % 4 == 0 or a % 400 == 0:
#     print("是闰年")
# else:
#     print("不是闰年")

#第四题
# weight = float(input("请输入体重:"))
# height = float(input("请输入身高:"))
# BMI = weight/height**2
# if BMI < 18.5:
#     print(BMI,"体重过轻")
# elif 18.5 <= BMI < 24:
#     print(BMI,"正常范围")
# elif BMI > 24:
#     print(BMI,"体重过重(超标)")



# for i in range(1,10):
#     for j in range(0,10):
#         for k in range(0,10):
#             if i*100+j*10+k==i**3+j**3+k**3:
#                 print(i*100+j*10+k)

# a = int(input("请输入第一个数字:"))
# b = int(input("请输入第一个数字:"))
# c = int(input("请输入第一个数字:"))
# d = int(input("请输入第一个数字:"))
# e = int(input("请输入第一个数字:"))
# if a==e and b==d:
#     print("是回文")
# else:
#     print("不是回文")

# a = int(input("请输入这组数:"))

# wan = a//10000
# qian = a%10000//1000
# bai = a%1000//100
# shi = a%100//10
# ge = a%10

# if wan == ge and qian == shi:
#     print(a,"是回文")
# else:
#     print(a,"不是回文")

