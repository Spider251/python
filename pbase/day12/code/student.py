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
    def remove_student(L):
        # n = input("请输入删除学生的姓名:")
        # del L[-1]
        pass
    def modify_student(L):
        # n = input("请输入学生的姓名:")
        # s = input("请输入学生的成绩:")
        # L[-1]['score'] = 60
        pass


            
        def print_score_desc(L):
            def get_score(d): # d为字典
                return d['score']
            #得到排序后的列表
            lst = sorted(L, key=get_score,reverse=True)
            print_student(lst)
        def print_score_asc(L):
            lst = sorted(L, 
                            key=lambda d:d['score']
                        )
            print_student(lst)
        def print_age_desc(L):
            lst = sorted(L, 
                            key=lambda d:d['age'],
                            reverse=True
                        )
            print_student(lst)
        def print_age_asc(L):
            lst = sorted(L, 
                            key=lambda d:d['age']
                        )
            print_student(lst)
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
                del_student(L)
            elif user_input == '4':
                xiugai_student(L)
            elif user_input == '5':
                print_score_desc(L)
            elif user_input == '6':
                print_score_asc(L)
            elif user_input == '7':
                print_age_desc(L)
            elif user_input == '8':
                print_age_asc(L)
    window()
main()