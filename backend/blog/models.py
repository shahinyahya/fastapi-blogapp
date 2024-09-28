from sqlalchemy import Integer, Column, String
from database import Base

#** Blog Model

class Blog(Base):

    __tablename__ = 'Blogs'

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String)
    body = Column(String)

#** User model

class User(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)