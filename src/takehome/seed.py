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
    {"name": "Apple", "quantity": 10},
    {"name": "Banana", "quantity": 20},
    {"name": "Orange", "quantity": 15},
    {"name": "Potato Chips", "quantity": 8}
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
                existing.quantity = data["quantity"]
                
        session.commit()
    
if __name__ == "__main__":
    seed_products()
