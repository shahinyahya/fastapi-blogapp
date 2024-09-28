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