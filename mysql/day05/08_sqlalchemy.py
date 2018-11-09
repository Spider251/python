from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,Integer,String
# session 会话
from sqlalchemy.orm import sessionmaker
# 创建数据库连接对象
engine = create_engine(
    "mysql+pymysql://root:123456@localhost/db5")
# 创建一个ORM基类
Base = declarative_base()

session = sessionmaker(engine)()

class User(Base):
    __tablename__ = 't123'
    id = Column(Integer,primary_key=True)
    name = Column(String(20))
    phnumber = Column(String(11),unique=True)

    def add_data(self):
        p = User(id=1,name="Lucy",phnumber='1383838438')
        session.add(p)
        session.commit()

    def select_data(self):
        result = session.query(User).filter_by(id=1).all()

        for r in result:
            print(r.id,r.name)
Base.metadata.create_all(engine)

if __name__=='__main__':
    s = User()
    # s.add_data()
    s.select_data()