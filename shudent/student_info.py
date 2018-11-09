from menu import *
from student import *
def input_student(L):
    while True:      
        name = input("请输入姓名:")
        if not name:
            break
        while True:
            try:
                age = int(input("请输入年龄:"))
            except:
                continue
            else:
                break
        while True:
            try:
                score = int(input("请输入成绩:"))
            except:
                continue
            else:
                break
        L.append(Student(name,age,score))
    window()
def print_student(L):
    print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
    print("|"+'name'.center(10)+"|"+'age'.center(10)+'|'+'score'.center(10)+"|")
    print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
    for i in L:
        n, z, s = i.get_info()
        a = '|'+n.center(10)
        a += '|'+str(z).center(10)
        a += '|'+str(s).center(10)
        a += '|'
        print(a)
    print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
def deL_student(L):
    n, z, s = i.get_info()
    x = input("请输入名字:")
    for index,i in enumerate(L):
        if x == n:
            L.remove(index)
            print("删除成功")
            window()
    else:
        print("您还没有添加此人")
        window()
def xiugai_student(L):
    x = input("请输入要修改的名字:")
    for index,i in enumerate(L):
        n, z, s = i.get_info()
        if x == n:
            score = input("请输入修改后的分数:")
            score =s
            print("修改成功")
            window()
        else:
            print("未查询到此人")
            window()  
#按照成绩升序
def student_score5(L): 
    L = sorted(L,key=lambda x:x.get_score())
    print_student(L)
#按照成绩降序
def student_score6(L): 
    L = sorted(L,key=lambda x:x.get_score(),reverse=True)
    print_student(L)
#查看字典内成绩键获得它的值
def student_age1(L): 
    L = sorted(L,key=lambda x:x.get_age())
    print_student(L)
def student_age2(L): 
    L = sorted(L,key=lambda x:x.get_age(),reverse=True)
    print_student(L)
def student_read():
    L = []
    try:
        rd = open("/home/tarena/AID1808/shudent/si.txt",'r')
        for line in rd:
            line = line.strip() # 去掉'\n'
            items = line.split(',')
            n, a, s = items
            a = int(a)
            s = int(s)
            L.append(Student(n,a,s))
        print("读取成功")
        rd.close()
    except OSError:
        print("打开文件失败")
    return L
def student_write(L):
    a = open("/home/tarena/AID1808/shudent/si.txt",'a')
    for i in L:
        i.write_to_file(a)
        # a.write(i.name)
        # a.write(",")
        # a.write(str(i.age))
        # a.write(",")
        # a.write(str(i.score))
        # a.write("\n")
    a.close()
    window()

