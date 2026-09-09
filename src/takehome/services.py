from sqlalchemy import select
from sqlalchemy.orm import Session
from takehome.models import Product, Reservation


class ProductService:
    def __init__(self, session: Session):
        self.session = session

    def get_all_products(self):
        return self.session.execute(select(Product)).scalars().all()
    


class ReservationService:
    def __init__(self, session: Session):
        self.session = session
        
    def get_reservation_by_id(self, reservation_id: int):
        return self.session.execute(select(Reservation).where(Reservation.id == reservation_id)).scalars().first()
    
    def create(self, product_id: int, quantity: int):
        pass
    
    def confirm(self, reservation_id: int):
        pass
    
    def release(self, reservation_id: int):
        pass