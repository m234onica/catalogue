from sqlalchemy import Column, String, Boolean, Date, DateTime, Integer, DECIMAL, Enum, func
from flask_login import UserMixin

from src.db import Base, db_session
import enum


class progress_Enum(enum.Enum):
    tbc = 0
    extra = 1
    end = 2


class Catalogs(Base):
    __tablename__ = 'catalogs'
    id = Column(Integer, nullable=False, primary_key=True, comment='書籍序號(主鍵)')
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment='建立時間')
    updatedAt = Column(DateTime, nullable=False,
                       server_default=func.now(), onupdate=func.now(), comment='更新時間')
    username = Column(String(50), nullable=False, comment="評書人")
    book = Column(String(100), nullable=False, comment='書名')
    author = Column(String(100), nullable=False, comment='作者')
    end_date = Column(Date, nullable=True, comment='完結日期')
    introduction = Column(String(1000), nullable=False, comment='簡介')
    review = Column(DECIMAL(2, 1), nullable=True, comment='評分')
    category = Column(String(50), nullable=True, comment='分類')
    progress = Column(Enum(progress_Enum), nullable=False, comment='連載或完結')
    article_source = Column(String(500), nullable=True, comment='文章連結')
    author_link = Column(String(500), nullable=True, comment='作者連結')

    def __repr__(self):
        return "<Catalogs: %r, %r, %r, %r, %r>" % (self.id, self.username, self.book, self.author, self.createdAt)


class Comments(Base):
    __tablename__ = 'comments'
    id = Column(Integer, nullable=False, primary_key=True, comment='主鍵')
    catalog_id = Column(Integer, nullable=False, comment='書籍序號')
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment='建立時間')
    updatedAt = Column(DateTime, nullable=False,
                       server_default=func.now(), onupdate=func.now(), comment='更新時間')
    username = Column(String(50), nullable=False, comment='留言者')
    review = Column(DECIMAL(2, 1), comment='評分')
    content = Column(String(6000), comment='留言內容')

    def __repr__(self):
        return "<Comments: %r, %r, %r, %r>" % (self.id, self.username, self.review, self.createdAt)


class Tags(Base):
    __tablename__ = 'tags'
    id = Column(Integer, nullable=False, primary_key=True, comment='主鍵')
    name = Column(String(50), nullable=False, comment='標籤名(主鍵)')
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment='建立時間')
    updatedAt = Column(DateTime, nullable=False,
                       server_default=func.now(), onupdate=func.now(), comment='更新時間')
    username = Column(String(50), nullable=False, comment='留言者')
    content = Column(String(500), nullable=True)

    def __repr__(self):
        return "<tags: %r, %r, %r, %r>" % (self.username, self.name, self.createdAt, self.content)


class Tags_Catalogs(Base):
    __tablename__ = 'tags_catalogs'
    id = Column(Integer, nullable=False, primary_key=True, comment='主鍵')
    tag_id = Column(Integer, nullable=False, comment='標籤序號')
    catalog_id = Column(Integer, nullable=False, comment='書籍序號')
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment='建立時間')
    updatedAt = Column(DateTime, nullable=False,
                       server_default=func.now(), onupdate=func.now(), comment='更新時間')

    def __repr__(self):
        return "<tags_catalogs: %r, %r>" % (self.tag_id, self.catalog_id)


class Users(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True, comment='主鍵')
    createdAt = Column(DateTime, nullable=False,
                       server_default=func.now(), comment='建立時間')
    updatedAt = Column(DateTime, nullable=False,
                       server_default=func.now(), onupdate=func.now(), comment='更新時間')
    username = Column(String(80), unique=True, nullable=False, comment='帳號')
    password = Column(String(120), nullable=False, comment='密碼')
    email = Column(String(100), unique=True, nullable=False, comment='信箱')
    fullname = Column(String(80), nullable=False, comment='本名')

    def __repr__(self):
        return "<users: %r, %r>" % (self.fullname, self.username)
