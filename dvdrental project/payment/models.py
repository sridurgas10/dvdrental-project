from sqlalchemy import Column, Integer, ForeignKey, Numeric, DateTime, func
from dbconnection import Base

class Payment(Base):
    __tablename__ = "payment"

    payment_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customer.customer_id"), nullable=False)
    staff_id = Column(Integer, ForeignKey("staff.staff_id"), nullable=False)
    rental_id = Column(Integer, ForeignKey("rental.rental_id"), nullable=False)
    amount = Column(Numeric(5,2), nullable=False)
    payment_date = Column(DateTime, server_default=func.now())
