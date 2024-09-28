from fastapi import FastAPI, Depends, status, Response, HTTPException
from schemas import Blog
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from typing import List
from hashing import Hash

""" This blog is for learning purpose so there will be no folder or file all services will be in main.py """

app = FastAPI()

#? Create a DataBase Table (i.e we are creating all models to the database as in activating it.)
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/', tags = ["Home"])
def home():
    return "This is my personal blog page"

@app.get("/blog", response_model=List[schemas.ShowBlog], tags = ["Blogs"])
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.post("/blog", status_code=status.HTTP_201_CREATED, tags = ["Blogs"])
def create_blog(blog: Blog, db: Session = Depends(get_db)):   #! here db parameter is used to get db from it using depends
    new_blog = models.Blog(author = blog.author, title = blog.title, body = blog.body, user_id = 1) #? creating new blog requesting each request data to model
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog/{id}", response_model=schemas.ShowBlog, tags = ["Blogs"])
def single_blog(id, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        #  response.status_code = status.HTTP_404_NOT_FOUND
        #  return "Blog not found!"
        raise HTTPException(status_code = 404, detail="The blog ain't found..")
    return blog


"""  
This is one way to delete a blog post. The other way is to delete using synchronize_session in sql alchemy which is show in next type
"""

# @app.delete("/blog/{id}", tags = ["Blogs"])
# def delete_blog(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
#     db.delete(blog)
#     db.commit()

#     return "The blog has deleted successfully."

#** Delete a blog

@app.delete('/blog/{id}', tags = ["Blogs"])
def destroy(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    
    return "The blog is deleted successfully"

#** Update a blog 

@app.put("/blog/{id}", tags = ["Blogs"])
def update_blog(id: int, req: schemas.BlogUpdate, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The requested blog with the id {id} has not been found")

    blog.title = req.title
    blog.body = req.body

    db.commit()
    db.refresh(blog)

    return "The blog has been updated successfully"

""" Here we are going to define Users to create. This will be the users section """

@app.get("/user", response_model = List[schemas.ShowUsers], tags = ["Users"])
def all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@app.get("/user/{id}", response_model = schemas.ShowUsers, tags = ["Users"])
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"The user id {id} not found")
    return user

@app.post("/user", tags = ["Users"])
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(username = request.username, email = request.email, password = Hash.password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)