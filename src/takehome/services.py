from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker
from takehome.models import Product, Reservation, Status


class ProductService:
    def __init__(self, session_maker: sessionmaker[Session]):
        self.session_maker = session_maker

    def get_all_products(self):
        with self.session_maker() as session:
            products = session.execute(select(Product)).scalars().all()
            reservations = session.scalars(select(Reservation).where(Reservation.status == Status.PENDING)).all()
        
            for product in products:
                product.available_quantity -= sum(reservation.quantity for reservation in reservations if reservation.product_id == product.id)
            return products

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
        return reservation
    
    def confirm(self, reservation_id: int):
        with self.session() as session:
            
            # here we also need to reduce available quantity of the product
            reservation = session.execute(select(Reservation).where(Reservation.id == reservation_id)).scalars().first()
            if not reservation:
                # TODO: robust error handling for missing reservation
                raise ValueError("Reservation not found")
            
            reservation.status = Status.CONFIRMED
            product = session.scalars(select(Product).where(Product.id == reservation.product_id)).first()
            if product:
                product.available_quantity -= reservation.quantity
                product.total_quantity -= reservation.quantity
                session.add(product)
            session.add(reservation)
        return reservation
    
    def release(self, reservation_id: int):
        # release cancels the reservation
        with self.session() as session:
            reservation = session.execute(select(Reservation).where(Reservation.id == reservation_id)).scalars().first()
            if not reservation:
                # TODO: robust error handling for missing reservation
                raise ValueError("Reservation not found")
            
            reservation.status = Status.CANCELLED
            session.add(reservation)
        return reservation