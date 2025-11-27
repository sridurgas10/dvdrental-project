from sqlalchemy.orm import Session
from . import models, schema
from dbconnection import engine
from sqlalchemy import text

def get_all_films(db: Session,limit: int ,offset: int ):
    return db.query(models.Film).limit(limit).offset(offset).all()

def get_film(db: Session, film_id: int):
    return db.query(models.Film).filter(models.Film.film_id == film_id).first()

def create_film(db: Session, film: schema.FilmCreate):
    new_film = models.Film(**film.model_dump())
    db.add(new_film)
    db.commit()
    db.refresh(new_film)
    return new_film

def update_film(db: Session, film_id: int, film: schema.FilmCreate):
    db_film = db.query(models.Film).filter(models.Film.film_id == film_id).first()
    if not db_film:
        return None
    for key, value in film.model_dump().items():
        setattr(db_film, key, value)
    db.commit()
    db.refresh(db_film)
    return db_film

def delete_film(db: Session, film_id: int):
    db_film = db.query(models.Film).filter(models.Film.film_id == film_id).first()
    if not db_film:
        return None
    db.delete(db_film)
    db.commit()
    return db_film


def film_availability(db: Session):
    query = text("SELECT * FROM film_availability")
    result = db.execute(query).mappings().all()  
    return result

def top_films(db:Session):
    query=text("select *from  top10_films" )
    result = db.execute(query).mappings().all()  
    return result