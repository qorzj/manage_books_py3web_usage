from sqlalchemy_plugin import obase
from sqlalchemy import Column, Integer, Numeric, String, DateTime


class Book(obase):
    __tablename__ = 'tbl_book'
    id = Column(Integer, primary_key=True)  # 图书ID
    name = Column(String(128))  # 书名
    author = Column(String(128))  # 作者
    press = Column(String(128))  # 出版社
    create_at = Column(DateTime)  # 创建时间
