# class_student.py

class Student:
    def __init__(self,name,age,score=0):
        
        self.name = name
        self.age = age
        self.score = score
    def set_score(self,score):
        self.score = score
        # print("成功修改成绩")
    def show_info(self):
        print(self.name,self.age,self.score)
L = []
L.append(Student("小张", 20, 100))
L.append(Student("小李", 18))
L.append(Student("小赵", 19, 85))
for s in L:
    s.show_info()
# L[1].set_score(70)
# L[1].show_info()