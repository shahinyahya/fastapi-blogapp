from fastapi import FastAPI
import models
from database import engine
from routers import blog, user, auth

""" This blog is for learning purpose so there will be no folder or file all services will be in main.py """

app = FastAPI()

#? Create a DataBase Table (i.e we are creating all models to the database as in activating it.)
models.Base.metadata.create_all(engine)

@app.get('/', tags = ["Home"])
def home():
    return "This is my personal blog page"

#! Include routers

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=80)
