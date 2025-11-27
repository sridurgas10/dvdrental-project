from sqlalchemy import Column, Integer, ForeignKey, DateTime, func
from dbconnection import Base

class Rental(Base):
    __tablename__ = "rental"

    rental_id = Column(Integer, primary_key=True, index=True)
    rental_date = Column(DateTime, server_default=func.now())
    inventory_id = Column(Integer)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    return_date = Column(DateTime, nullable=True)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"), nullable=False)
    last_update=Column (DateTime)