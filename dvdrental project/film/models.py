from sqlalchemy import Column, Integer, String, Float
from dbconnection import Base

class Film(Base):
    __tablename__ = "film"

    film_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(String)
    release_year = Column(Integer)
    language_id = Column(Integer)
    rental_duration = Column(Integer)
    rental_rate = Column(Float)
    length = Column(Integer)
    replacement_cost = Column(Float)
    rating = Column(String)
