from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
import schemas, models, database
from hashing import Hash
from sqlalchemy.orm import Session

router = APIRouter(prefix='/users', tags=["Users"])

get_db = database.get_db

""" Here we are going to define Users to create. This will be the users section """

@router.get("/", response_model = List[schemas.ShowUsers])
def all_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}", response_model = schemas.ShowUsers)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"The user id {id} not found")
    return user

@router.post("/")
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    new_user = models.User(username = request.username, email = request.email, password = Hash.password_hash(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user