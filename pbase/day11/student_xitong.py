def main():
    L = [] # 用于保存学生信息
    def input_student():
        while True:
            d = {} # 用于保存单个学生信息
            name = input("请输入姓名:")
            if not name:
                break
            age = int(input("请输入年龄:"))
            score = int(input("请输入成绩:"))
            d['name'] = name #输入名字填写到字典中
            d['age'] = age
            d['score'] = score
            L.append(d) # 将每个学生的信息追加到L列表内
        return L
    def print_student(l):
        print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
        print("|"+'name'.center(10)+"|"+'age'.center(10)+'|'+'score'.center(10)+"|")
        print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
        for i in l:
            a = '|'+i['name'].center(10)
            a += '|'+str(i['age']).center(10)
            a += '|'+str(i['score']).center(10)
            a += '|'
            print(a)
        print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
    def del_student():
        x = input("请输入名字:")
        for i in L:
            if x == i['name']:
                L.remove(i)
                print("删除成功")
                window()
        else:
            print("您还没有添加此人")
            window()
    def xiugai_student():
        x = input("请输入要修改的名字:")
        for i in L:
            if x == i['name']:
                score = input("请输入修改后的分数:")
                i['score'] = score
                print("修改成功")
                window()
            else:
                print("未查询到此人")
                window()  
    #按照成绩升序
    def student_score5(): 
        l = sorted(L,key=get_score)
        print_student(l)
        return l
    #按照成绩降序
    def student_score6(): 
        l = sorted(L,key=get_score,reverse=True)
        print_student(l)
        return l
    #查看字典内成绩键获得它的值
    def get_score(x):
        return x['score']
    def student_age1(): 
        l = sorted(L,key=get_age)
        print_student(l)
        return l
    def student_age2(): 
        l = sorted(L,key=get_age,reverse=True)
        print_student(l)
        return l
    def get_age(x):
        return x['age']
    
    def window():
        global L
        L = []#用于保存学生信息的列表
        while True:
            print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
            print("|(1) 添加学生信息                "+"|")
            print("|(2) 显示学生信息                "+"|")
            print("|(3) 删除学生信息                "+"|")
            print("|(4) 修改学生信息                "+"|")
            print('|(5) 按学生成绩高-低显示学生信息 '+'|')
            print('|(6) 按学生成绩低-高显示学生信息 '+'|')
            print('|(7) 按学生年龄高-低显示学生信息 '+'|')
            print('|(8) 按学生年龄低-高显示学生信息 '+'|')
            print("|(q) 退出                        "+"|")
            print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
            user_input = input("请选择:")
            if user_input == 'q':
                break
            elif user_input == '1':
                L += input_student()
            elif user_input == '2':
                print_student(L)
            elif user_input == '3':
                del_student()
            elif user_input == '4':
                xiugai_student()
            elif user_input == '5':
                student_score5()#升序
            elif user_input == '6':
                student_score6()#降序
            elif user_input == '7':
                student_age1()#升序
            elif user_input == '8':
                student_age2()#降序
    window()
main()