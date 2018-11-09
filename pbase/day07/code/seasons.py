# seasons.py

# 1.
# seasons = {1:'春季有1,2,3月',2:'夏季有4,5,6月',3:'秋季有7,8,9月',4:'冬季有10，11,12月'}
# print(seasons)

#2.
d = int(input("请输入一个整数:"))
seasons = {1:'春季有1,2,3月',
            2:'夏季有4,5,6月',
              3:'秋季有7,8,9月',
                4:'冬季有10，11,12月'}
if d in seasons:
    print(seasons[d])
else:
    print("信息不存在")
    

