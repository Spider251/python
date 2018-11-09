# price.py
#方法1
'''
d = input("请输入一段文字:")
c = {}
for i in d:
    # 1.没有出现过 值+1
    if i not in c:
        c[i] = 1
    #除去第一次,出现过几次,值反复加1
    else:
        c[i] = c[i]+1 #c[i] += 1
#打印结果
for i in c:
    print(i,"出现了",c[i],'次')
'''
# 方法2
#先将字符串去重,放入到列表L中
s = input("请输入一段文字:")
L = []#用来存放出现过的字符
for ch in s:
    #如果ch没有在L中,说明第一次出现,放入到L中
    if ch not in L:
        L.append(ch)
for ch in L:
    print(ch,":",s.count(ch),'次')

        