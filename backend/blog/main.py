from fastapi import FastAPI, Depends, status, Response, HTTPException
from schemas import Blog
import schemas, models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

#? Create a DataBase Table (i.e we are creating all models to the database as in activating it.)
models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/')
def home():
    return "This is my personal blog page"

@app.post("/blog", status_code=status.HTTP_201_CREATED)
def create_blog(blog: Blog, db: Session = Depends(get_db)):   #! here db parameter is used to get db from it using depends
    new_blog = models.Blog(author = blog.author, title = blog.title, body = blog.body) #? creating new blog requesting each request data to model
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog")
def get_all_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@app.get("/blog/{id}")
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

# @app.delete("/blog/{id}")
# def delete_blog(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
#     db.delete(blog)
#     db.commit()

#     return "The blog has deleted successfully."

#** Delete a blog

@app.delete('/blog/{id}')
def destroy(id: int, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    
    return "The blog is deleted successfully"

#** Update a blog 

@app.put("/blog/{id}")
def update_blog(id: int, blog: schemas.BlogUpdate, db: Session = Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).update({blog}, synchronize_session=False)
    db.commit()
    return "The blog has been updated"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)