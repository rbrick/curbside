from fastapi import FastAPI
from takehome.services import ProductService
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from takehome.models import Base
from dotenv import load_dotenv

import os

load_dotenv() # load our environment variables from a .env

# create instance of the fast api app
app = FastAPI()

# create the database engine instance
engine = create_engine(os.getenv("DB_URL"))

Session = sessionmaker(engine)

def init_db():
    Base.metadata.create_all(engine)


product_service = ProductService(Session()) 

@app.get("/products")
def get_products():
    """
    Retrieves live list of products from the database.
    """
    return product_service.get_all_products()