import pymysql

db = pymysql.connect(host="localhost",user="root",password="123456",database="db5",charset="utf8")

cursor = db.cursor()
try:
    sel = "select * from t1"
    #得到一堆查询结果,放到两cursor游标对象里
    cursor.execute(sel)
    data1 = cursor.fetchone()
    print(data1)
    #(1, '李白', 100.0)
    print("*" * 40)
    #取走游标对象里的多条记录
    data2 = cursor.fetchmany(2)
    for i in data2:
        print(i)
    #(2, '杜甫', 70.0)
    #(3, '白居易', 80.0)
    print("*" * 40)
    #取走游标对象中剩下的表记录
    data3 = cursor.fetchall()
    print(data3)
    #((5, '钟无艳', 11.0),)
except Exception as e:
    print("Failed",e)

cursor.close()
db.close()
