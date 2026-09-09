from sqlalchemy import select
from takehome.models import Product


class ProductService:
    def __init__(self, session):
        self.session = session

    def get_all_products(self):
        return self.session.execute(select(Product)).scalars().all()