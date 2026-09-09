from fastapi import FastAPI
from sqlalchemy import create_engine
from takehome.models import Base
from dotenv import load_dotenv

import os

load_dotenv() # load our environment variables from a .env

# create instance of the fast api app
app = FastAPI()

# create the database engine instance
engine = create_engine(os.getenv("DB_URL"))

def init_db():
    Base.metadata.create_all(engine)


