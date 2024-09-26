from fastapi import FastAPI, Depends
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

@app.post("/blog")
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
    return blog


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)