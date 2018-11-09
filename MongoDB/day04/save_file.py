from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)
db = conn.image # 进入数据库
myset = db.flower # 生成集合对象

# 存储图片
f = open('/home/tarena/AID1808/MongoDB/day04/mm.jpg','rb')
data = f.read()

# 将data转换为mongodb存储格式
content = bson.binary.Binary(data)

# 插入到文档

# 插入到集合
# myset.insert({'filename':'gril.jpg','data':content})

# 文件提取
img = myset.find_one({'filename':'gril.jpg'})

# 将data域内容写入本地文件
with open('plmm.jpg','wb') as f:
    f.write(img['data'])

conn.close()