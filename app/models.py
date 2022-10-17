from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session
from app.config import DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={})
    session = Session(bind=engine.connect())
    return session


class references_table(Base):
    __tablename__ = 'references_table'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    descript = Column(String)


class news_table(Base):
    __tablename__ = 'news_table'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    descript = Column(String)
    region = Column(String)


class gum_help_table(Base):
    __tablename__ = 'gum_help_table'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    address = Column(String)
    timing = Column(String)
