from pydantic import BaseModel
from datetime import datetime
from typing import List

class CategoryBase(BaseModel):
  name:str
  last_update:datetime

class CategoryCreate(CategoryBase):
  pass

class CategoryOut(CategoryBase):
  category_id:int
  class config:
    orm_mode=True

class PaginatedCategory(BaseModel):
    category: List[CategoryOut]
    page: int
    limit: int
    total_pages: int
    next_page: int 
    previous_page: int 