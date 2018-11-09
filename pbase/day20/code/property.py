# property.py


class Student:
    def __init__(self, s):
        self.score = s  # 成绩
    def get_score(self):
        '''getter'''
        return self.__score
    def set_score(self):
        '''setter'''
        assert 0 <= s <= 100, '成绩超出范围'
        self.__score = s

s1 = Student(59)
print(s1.get_score())
s1.score = 9999999999999  # 赋值
# print(s1.score)  # 取值
