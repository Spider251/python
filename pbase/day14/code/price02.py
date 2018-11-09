# price02.py


def get_age():
    score = int(input("请输入你的年龄:"))
    if 0 > score or score > 140:
        raise ValueError
    return score
try:    
    age = get_age()
    print("用户输入的年龄是:",age)
except ValueError as err:
    print("你特码多大心里没点B数吗,爱玩玩,不玩歌舞恩")
    
