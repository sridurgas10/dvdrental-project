from pydantic import BaseModel
from datetime import datetime
from typing import List

class CustomerBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    store_id :int
    address_id :int
    activebool:bool
    create_date :datetime
    last_update :datetime

class CustomerCreate(CustomerBase):
    pass    

class CustomerOut(CustomerBase):
    customer_id: int
    class config:
        orm_mode=True

class PaginatedCustomer(BaseModel):
    customers: List[CustomerOut]
    page: int
    limit: int
    total_pages: int
    next_page: int 
    previous_page: int           

class TopCustomer(BaseModel):
    customer_id:int
    first_name:str
    last_name:str  
    total_amount:float    

class CustomerRental(BaseModel):
    customer_id:int
    total_rentals:int
    total_payment:float

class RentalCost(BaseModel):
    customer_id: int
    total_rental_cost: float
