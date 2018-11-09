# price02.py
# names = ['Tom','Jerry','Spike','Tyke']
# 排序的依据是:'moT','yrreJ','ekipS','ekyT'
# 结果是:
#     [Spike, Tyke, 'To,, Jerry]
names = ['Tom','Jerry','Spike','Tyke']
def my(x):
    x = x[::-1]
    print(x)
    return x
L1 = sorted(names,key=my)
print(L1)