from sqlalchemy import Integer, Column, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship

#** Blog Model

class Blog(Base):

    __tablename__ = 'Blogs'

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String)
    title = Column(String)
    body = Column(String)
    user_id = Column(Integer, ForeignKey("Users.id"))  #** connecting each blogs with user_id using foreign key.

    #? Every blog post should relate to a user
    creator = relationship("User", back_populates='blogs')

#** User model

class User(Base):

    __tablename__ = "Users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

    #? Each users have multiple blogs

    blogs = relationship("Blog", back_populates='creator')