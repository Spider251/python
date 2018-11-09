# week.py
# 1. 模拟斗地主发牌,扑克牌54张
#     花色:
#       黑桃('\u2660'), 梅花('\u2663'), 红桃('\u2665'), 方块('\u2666')
#     数字:
#       A2-10JQK
#     大王,小王

#   三个人,每个人发17张牌,底牌留三张
#     输入回车,打印第1个人的17张牌
#     输入回车,打印第2个人的17张牌
#     输入回车,打印第3个人的17张牌
#     输入回车,打印3张底牌


#1  against_landlord斗地主
# def against_landlord():
#     import random
#     color = ['\u2660','\u2663','\u2665','\u2666']
#     wang = ['大王','小王']
#     a = ['A']+[str(x) for x in range(2, 11)] + list("JQK")
#     s = [i+j for i in color for j in a]
#     s += wang
#     one = random.sample(s,17)
#     for i in one:
#         s.remove(i)
#     two = random.sample(s,17)
#     for i in two:
#         s.remove(i)
#     three = random.sample(s,17)
#     for i in three:
#         s.remove(i)
#     dipai = s
#     z = input("请取第一个人的牌(yes/no)")
#     if z == 'yes':
#         print(one)
#     z = input("请取第二个人的牌(yes/no)")
#     if z == 'yes':
#         print(two)
#     z = input("请取第三个人的牌(yes/no)")
#     if z == 'yes':
#         print(three)
#     z = input("是否查看底牌(yes/no)")
#     if z == 'yes':
#         print(dipai)
# against_landlord()


poke = ['joker','Joker']
kinds = ['\u2660','\u2663','\u2665','\u2666']
numbers = ['A']+[str(x) for x in range(2, 11)] + list("JQK")

for i in kinds:
    for j in numbers:
        poke.append(i+j)

poke2 = poke.copy()
#洗牌
import random
random.shuffle(poke2)

play1 = poke2[:17] #发给玩家1
play2 = poke2[17:34] #发给玩家2
play3 = poke2[34:51] #发给玩家3
dipai = poke2[51:] # dipai==底牌
poke2.clear() #del poke2

#   三个人,每个人发17张牌,底牌留三张
input("请输入回车键发给第一个人：")
print(play1)
#     输入回车,打印第1个人的17张牌
input("请输入回车键发给第二个人：")
print(play2)
#     输入回车,打印第2个人的17张牌
input("请输入回车键发给第三个人：")
print(play3)
#     输入回车,打印第3个人的17张牌
input("请输入回车键发底牌：")
print(dipai)
#     输入回车,打印3张底牌





