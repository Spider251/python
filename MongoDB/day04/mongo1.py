from pymongo import MongoClient

conn = MongoClient('localhost',27017)
cnn = conn.stu
myset = cnn.class0

# 创建索引
# index_name = myset.create_index('name')
# print(index_name)

# index_name = myset.create_index([('age',-1)])

#查看索引
for i in myset.list_indexes():
    print(i)

#删除索引
# myset.drop_index('name_1')

#删除所有索引
# myset.drop_indexes()

#其他索引类型
# index = myset.create_index('name',unique=True,sparse=True)


conn.close()

