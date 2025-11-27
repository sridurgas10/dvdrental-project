from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbconnection import get_db
from . import crud, schema,models

film_router = APIRouter(prefix="/films", tags=["Films"])

'''@film_router.get("/", response_model=list[schema.FilmOut])
def list_films( limit: int ,offset: int ,db: Session = Depends(get_db)):
    return crud.get_all_films(db, limit, offset)'''

@film_router.get("/", response_model=schema.PaginatedFilms)
def list_films(page: int , limit: int , db: Session = Depends(get_db)):
    offset = page  * limit
    films = crud.get_all_films(db, limit, offset)
    
    total = db.query(models.Film).count()  
    total_pages = (total + limit - 1) // limit


    return {
        "films": films,
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "next_page": page + 1 if page < total_pages else None,
        "previous_page": page - 1 if page > 1 else None
    }

@film_router.get("/{film_id}", response_model=schema.FilmOut)
def get_film(film_id: int, db: Session = Depends(get_db)):
    film = crud.get_film(db, film_id)
    if not film:
        raise HTTPException(status_code=404, detail="Film not found")
    return film

@film_router.post("/films/", response_model=schema.FilmOut)
def create_film(film: schema.FilmCreate, db: Session = Depends(get_db)):
    return crud.create_film(db, film)

@film_router.put("/films/{film_id}", response_model=schema.FilmOut)
def update_film(film_id: int, film: schema.FilmCreate, db: Session = Depends(get_db)):
    updated = crud.update_film(db, film_id, film)
    if not updated:
        raise HTTPException(status_code=404, detail="Film not found")
    return updated

@film_router.delete("/films/{film_id}", response_model=schema.FilmOut)
def delete_film(film_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_film(db, film_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Film not found")
    return deleted

# Film availability from view
@film_router.get("/availability/", response_model=list[schema.FilmAvailabilityView])
def available_films(db: Session = Depends(get_db)):
    return crud.film_availability(db)


@film_router.get("/reports/top_films/",response_model=list[schema.TopFilms])
def rented_film(db:Session=Depends(get_db)):
    return crud.top_films(db)