# property.py


class Student:
    def __init__(self, s):
        self.__score = s  # 成绩
    @property
    def score(self):
        '''getter'''
        return self.__score
    @score.setter
    def score(self, s):
        '''setter'''
        assert 0 <= s <= 100, '成绩超出范围'
        self.__score = s

s1 = Student(59)
print(s1.score)
# s1.score = 100111111111  # 报错
s1.score = 100  # 赋值
print(s1.score)  # 取值