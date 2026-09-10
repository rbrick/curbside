from fastapi import FastAPI
from takehome.services import ProductService, ReservationService
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


product_service = ProductService(Session) 
reservation_service = ReservationService(Session)

@app.get("/products")
def get_products():
    """
    Retrieves live list of products from the database.
    """
    return product_service.get_all_products()


@app.post("/reservations")
def create_reservation(product_id: int, quantity: int):
    """
    Creates a new reservation for a given product and quantity.
    """
    return reservation_service.create(product_id, quantity)

@app.get("/reservations/{reservation_id}")
def get_reservation(reservation_id: int):
    """
    Retrieves a reservation by its ID.
    """
    return reservation_service.get_reservation_by_id(reservation_id)

@app.post("/reservations/{reservation_id}/confirm")
def confirm_reservation(reservation_id: int):
    """
    Confirms a reservation by its ID.
    """
    return reservation_service.confirm(reservation_id)

@app.post("/reservations/{reservation_id}/release")
def release_reservation(reservation_id: int):
    """
    Releases (cancels) a reservation by its ID.
    """
    return reservation_service.release(reservation_id)