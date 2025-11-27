from sqlalchemy import Column, Integer, String, Boolean, DateTime
from dbconnection import Base

class Category(Base):
    __tablename__ = "category"

    category_id = Column(Integer, primary_key=True, index=True)
    name= Column(String)
    last_update = Column(DateTime)
