import menu
import student_info as c
menu.window()
#学生管理系统的主模块
def main():
    L=[]
    while True:
        user_input = input("请选择:")
        if user_input == 'q':
            break
        elif user_input == '1':
            c.input_student(L)
        elif user_input == '2':
            c.print_student(L)
        elif user_input == '3':
            c.deL_student(L)
        elif user_input == '4':
            c.xiugai_student(L)
        elif user_input == '5':
            c.student_score5(L)#升序
        elif user_input == '6':
            c.student_score6(L)#降序
        elif user_input == '7':
            c.student_age1(L)#升序
        elif user_input == '8':
            c.student_age2(L)#降序
        elif user_input == '9':
            L = c.student_read()
        elif user_input == '10':
            c.student_write(L)
main()