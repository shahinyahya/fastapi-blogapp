from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#** Database url is stored 
BLOG_DATABASE_URL = 'sqlite:///./blog.db'

# ** Startup engine to initiate Database
engine = create_engine(BLOG_DATABASE_URL, connect_args={"check_same_thread": False})

#** Create a Session in order to interact with the database
SessionLocal = sessionmaker(bind= engine, autocommit = False, autoflush = False)

#** Create declarative base to declare ORM 
Base = declarative_base()

