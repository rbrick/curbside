from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select


from takehome.models import Base, Product



load_dotenv()

engine = create_engine(os.getenv("DB_URL"))
Session = sessionmaker(engine)

products = [
    {"name": "Apple", "total_quantity": 10, "available_quantity": 10, "price_cents": 100},
    {"name": "Banana", "total_quantity": 20, "available_quantity": 20, "price_cents": 50},
    {"name": "Orange", "total_quantity": 15, "available_quantity": 15, "price_cents": 75},
    {"name": "Potato Chips", "total_quantity": 8, "available_quantity": 8, "price_cents": 300}
]

def seed_products():
    with Session() as session:
        for data in products:
            existing = session.scalar(
                select(Product).where(Product.name == data["name"])
            )
            if not existing:
                session.add(Product(**data))
            else: 
                existing.available_quantity = data["available_quantity"]
                existing.total_quantity = data["total_quantity"]
                existing.price_cents = data["price_cents"]
                
        session.commit()
    
if __name__ == "__main__":
    seed_products()
