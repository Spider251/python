from mysqlpython import Mysqlpython

sqlh = Mysqlpython("db5")
dele = "delete from t1 where name='" "'"
sqlh.zhixing(dele)