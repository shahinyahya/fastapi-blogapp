from pydantic import BaseModel
from typing import List, Optional

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
    creator: ShowUsers

class Login(BaseModel):
    username: str
    password: str

#! Create Schema for token and token required for JWT

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None