def main():
    L = []
    def input_student():
        while True:
            d = {}
            name = input("请输入姓名:")
            if not name:
                break
            age = int(input("请输入年龄:"))
            score = int(input("请输入成绩:"))
            d['name'] = name
            d['age'] = age
            d['score'] = score
            L.append(d)
        return L
    def print_student():
        print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
        print("|"+'name'.center(10)+"|"+'age'.center(10)+'|'+'score'.center(10)+"|")
        print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
        for i in L:
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
    def window():
        global L
        L = []#用于保存学生信息的列表
        while True:
            print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
            print("| 1) 添加学生信息                "+"|")
            print("| 2) 显示学生信息                "+"|")
            print("| 3) 删除学生信息                "+"|")
            print("| 4) 修改学生信息                "+"|")
            print("| q) 退出                        "+"|")
            print("+"+'-'*10+"+"+'-'*10+'+'+'-'*10+"+")
            user_input = input("请选择:")
            if user_input == 'q':
                break
            elif user_input == '1':
                L += input_student()
            elif user_input == '2':
                print_student()
            elif user_input == '3':
                del_student()
            elif user_input == '4':
                xiugai_student()
    window()
main()




    


    



    


