from pydantic import BaseModel
from typing import List

class FilmBase(BaseModel):
    title: str
    description: str 
    release_year: int 
    language_id: int 
    rental_duration: int
    rental_rate: float 
    length: int 
    replacement_cost: float 
    rating: str

class FilmCreate(FilmBase):
    pass

class FilmOut(FilmBase):
    film_id: int
  
    class config:
        orm_mode=True

class FilmAvailabilityView(BaseModel):
    film_id: int
    title: str
    total_stock:int
    rented_count:int 
    available_stock: int
    

class TopFilms(BaseModel):
    film_id:int
    title:str
    rental_count:int
           

class PaginatedFilms(BaseModel):
    films: List[FilmOut]
    page: int
    limit: int
    total_pages: int
    next_page: int 
    previous_page: int     
  