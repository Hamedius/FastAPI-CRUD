from sqlalchemy import Column, Integer, String
from .database import Base


class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)
    national_id = Column(String)

class Product(Base):
    __tablename__ = 'Product'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(String)
    name = Column(String)
    price = Column(Integer)
    description = Column(String)
