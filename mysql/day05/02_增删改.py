'''
在t1表中增加1条记录 
在t1表中把李白的成绩改为100分
在t1表中删除1条记录

'''

import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",database="db5",charset="utf8")

cursor = db.cursor()
try:
    cursor.execute('insert into t1 values(5,"钟无艳",11);')
    cursor.execute('update t1 set score=100 where name="李白";')
    cursor.execute('delete from t1 where name="王维";')
    db.commit()
    print("OK")
except Exception as e:
    db.rollback()
    print("Failed",e)


cursor.close()
db.close()
