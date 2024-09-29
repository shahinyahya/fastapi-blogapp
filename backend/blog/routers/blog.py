from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
import schemas, models, database
from sqlalchemy.orm import Session
from oauth2 import get_current_user

router = APIRouter(prefix="/blog", tags=["Blogs"])

get_db = database.get_db

@router.get("/", response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_blog(req: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):   #! here db parameter is used to get db from it using depends
    new_blog = models.Blog(author = req.author, title = req.title, body = req.body, user_id = 1) #? creating new blog requesting each request data to model
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@router.get("/{id}", response_model=schemas.ShowBlog)
def single_blog(id, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        #  response.status_code = status.HTTP_404_NOT_FOUND
        #  return "Blog not found!"
        raise HTTPException(status_code = 404, detail="The blog ain't found..")
    return blog

"""  
This is one way to delete a blog post. The other way is to delete using synchronize_session in sql alchemy which is show in next type
"""

# @router.delete("/{id}")
# def delete_blog(id: int, db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
#     db.delete(blog)
#     db.commit()

#     return "The blog has deleted successfully."

#** Delete a blog

@router.delete('/{id}')
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    
    return "The blog is deleted successfully"

#** Update a blog 

@router.put("/{id}")
def update_blog(id: int, req: schemas.BlogUpdate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The requested blog with the id {id} has not been found")

    blog.title = req.title
    blog.body = req.body

    db.commit()
    db.refresh(blog)

    return "The blog has been updated successfully"