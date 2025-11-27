from sqlalchemy import Column, Integer, String, Boolean, DateTime
from dbconnection import Base

class Customer(Base):
    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True)
    store_id = Column(Integer)
    address_id = Column(Integer)
    activebool = Column(Boolean)
    create_date = Column(DateTime)
    last_update = Column(DateTime)
