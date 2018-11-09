# price01.py
# 方法1 在调用get_score时加入try语句
# def get_score():  
#     a = int(input("请输入成绩:"))
#     if not (0 <= a <= 100):
#         return 0
#     return a
# try:
#     score = get_score()
# except ValueError:
#     #如果未获取到学生信息,则此时学生成绩为0
#     score = 0
# print("您输入的成绩是:",score)

#方法2 在get_score函数内部加入try语句来进行错误处理
def get_score():
    try:
        s = int(input("请输入成绩:"))
    except ValueError:
        return 0
    if not (0 <= s <= 100):
        return 0
    return s
score = get_score()
print("您输入的成绩是:",score)

