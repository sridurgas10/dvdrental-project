from sqlalchemy import Column, Integer, String
from dbconnection import Base  
from sqlalchemy import (
    Column, Integer, String, Boolean, SmallInteger,
    TIMESTAMP, LargeBinary, text
)


class StaffUser(Base):
    __tablename__ = "staff"

    staff_id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)

    address_id = Column(SmallInteger)

    email = Column(String())
    store_id = Column(SmallInteger, nullable=False)

    active = Column(Boolean, nullable=False, server_default=text("true"))

    username = Column(String(), nullable=False)
    password = Column(String())        

    last_update = Column(TIMESTAMP, nullable=False, server_default=text("now()"))
