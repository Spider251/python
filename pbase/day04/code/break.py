# break.py


i = 1
while i <= 6:
    print("本次循环开始,i=",i)
    if i == 3:
        break #结束当前while语句的执行
    print("本次循环结束，i=",i)
    i += 1
print("循环结束")
