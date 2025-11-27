from pydantic import BaseModel
from datetime import datetime
from typing import List,Optional

class RentalBase(BaseModel):
    inventory_id: int
    customer_id: int
    staff_id: int
    rental_date: datetime
    return_date:datetime
    last_update:datetime

class RentalCreate(RentalBase):
    pass 


class RentalOut(RentalBase):
    rental_id: int
    class config:
        orm_mode=True


class PaginatedRental(BaseModel):
    rental:List[RentalOut]
    page:int
    limit:int
    total_pages:int
    next_page:int
    previous_page:int

class OverdueRental(BaseModel):
    rental_id: int
    inventory_id: int
    customer_id: int
    staff_id: int
    rental_date: datetime
    return_date:Optional[datetime]
    last_update:datetime
   
class StaffPerformance(BaseModel):
    staff_id:int
    total_rentals:int

