from pydantic import BaseModel
from datetime import datetime

class StaffBase(BaseModel):
    username: str
    password: str
    email: str
    first_name:str
    last_name:str
    store_id:int
    active:bool
    last_update:datetime
    address_id:int

class StaffCreate(StaffBase):
    pass


class StaffOut(StaffBase):
    staff_id: int
    email:str
    class config:
        orm_mode=True

class StaffLogin(BaseModel):
    username: str
    email:str
    password: str

class StaffMe(BaseModel):
    token:str    

class Token(BaseModel):
    access_token: str
    token_type: str

class StaffPerformance(BaseModel):
    staff_id:int
    count:int