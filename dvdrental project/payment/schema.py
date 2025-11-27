from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal
from typing import List

class PaymentBase(BaseModel):
    customer_id: int
    staff_id: int
    rental_id: int
    amount: Decimal
    payment_date: datetime

class PaymentCreate(PaymentBase):
    pass

class PaymentOut(PaymentBase):
    payment_id: int
    class config:
        orm_mode=True

class PaginatedPayment(BaseModel):
    payment:List[PaymentOut]
    page:int
    limit:int
    total_pages:int
    next_page:int
    previous_page:int
