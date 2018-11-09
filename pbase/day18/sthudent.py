# class_student.py

class Student:
    infos = []
    def __init__(self,name,age,score=0):
        self.name = name
        self.age = age
        self.score = score
    @classmethod
    def input_student(cls):
        while True:
            n = input("请输入姓名:")
            if not n:
                break
            a = int(input("请输入年龄:"))
            s = int(input("请输入成绩:"))
            cls.infos.append(Student(n,a,s))
    @classmethod
    def del_student(cls):
        n = input("请输入要删除学生的姓名:")
        for index, s in enumerate(cls.infos):
            if s.name == n:
                del cls.infos[index]
                return 
    @classmethod
    def print_student_count(cls):
        print("学生的个数: ",len(cls.infos)) 
    @classmethod
    def print_avg_score(cls):
        total_score = sum((s.score for s in cls.infos))
        # total_score = 0
        # for s in cls.infos:
        #     total_score += s.score
        print("平均成绩是:",total_score/len(cls.infos))
    @classmethod
    def output_student(cls):
        for s in cls.infos:
            print(s.name,s.age,s.score)


Student.input_student()
Student.output_student()
Student.del_student()
Student.output_student()
Student.print_student_count()
Student.print_avg_score()
