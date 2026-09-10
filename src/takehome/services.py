from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from takehome.models import Product, Reservation, Status


class ProductService:
    def __init__(self, session_maker: sessionmaker[Session]):
        self.session = session_maker

    def get_all_products(self):
        with self.session() as session:
            return session.execute(select(Product)).scalars().all()
    


class ReservationService:
    def __init__(self, session_maker: sessionmaker[Session]):
        self.session = session_maker
        
    def get_reservation_by_id(self, reservation_id: int):
        with self.session() as session:
            return session.execute(select(Reservation).where(Reservation.id == reservation_id)).scalars().first()
    
    def get_reserved_quantity(self, product_id: int):
        with self.session() as session:
            product = session.scalars(select(Product).where(Product.id == product_id)).first()
            if not product:
                # TODO: robust error handling for missing product
                raise ValueError("Product not found")
            
            reservations = session.scalars(select(Reservation).where((Reservation.product_id == product_id) & (Reservation.status == Status.PENDING))).all()
            reserved_quantity = sum(reservation.quantity for reservation in reservations)
            
            return reserved_quantity
        
    
    def create(self, product_id: int, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")
    
        with self.session() as session:
            product = session.scalars(
                    select(Product).where(Product.id == product_id)).first()
                
            if not product:
                # TODO: robust error handling for missing product
                raise ValueError("Product not found")
            
            reserved_quantity = self.get_reserved_quantity(product_id)
            if reserved_quantity + quantity > product.available_quantity:
                # TODO: robust error handling for insufficient stock
                raise ValueError("Insufficient stock")
            
            reservation = Reservation(product_id=product_id, quantity=quantity) # make a reservation
            session.add(reservation)
        pass
    
    def confirm(self, reservation_id: int):
        pass
    
    def release(self, reservation_id: int):
        pass