# Fastapi Blog API

## Folder Structure

---

`- blog/
- ├── blog.db             ##---> This is the blog database creaed with sqlite
- ├── hashing.py          ##---> File for creating and validating hashed passwords
- ├── jwttoken.py         ##---> File for creating JWT for user auth and validating the token till expiry
- ├── models.py           ##---> Models for user blog using ORM SQLAlchemy
- ├── schemas.py          ##---> Described data structure for models
- ├── database.py         ##---> Acvtivating Database in order to run
- ├── main.py             ##---> Main app file to run the app
- ├── oauth2.py           ##---> Getting current active user to validate each endpoint if user is logged in or not 
- ├── requirements.txt    ##---> Required packages for the app
- ├── __init__.py
- └── routers/            ##---> This directory is used creating router for each (blog and users)
    - ├── auth.py
    - ├── blog.py
    - ├── __init__.py
    - └── user.py`

---

### How to set up

1. Go to blog folder and install python virtual environment `python -m venv venv`
2. Then run `pip install -r requirements.txt`
3. Run main.py file `python main.py`
4. App is ready to use.
