from pydantic import BaseModel
from typing import List

#** Schema for users

class Blog(BaseModel):
    author: str
    title: str
    body: str

class User(BaseModel):
    username: str
    email: str
    password: str
    

class ShowUsers(BaseModel):
    username: str
    email: str
    blogs: List[Blog] = []

#** Update blog schema

class BlogUpdate(BaseModel):
    title: str
    body: str

class ShowBlog(Blog):
    author: str
    title: str
    body: str
    creator: ShowUsers