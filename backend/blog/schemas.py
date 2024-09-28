from pydantic import BaseModel


#? Creating a blog
class Blog(BaseModel):
    author: str
    title: str
    body: str

#** Update blog schema

class BlogUpdate(BaseModel):
    title: str
    body: str

class ShowBlog(Blog):
    pass

#** Schema for users

class User(BaseModel):
    username: str
    email: str
    password: str

class ShowUsers(BaseModel):
    username: str
    email: str