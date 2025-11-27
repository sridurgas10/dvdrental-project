from sqlalchemy.orm import Session
from . import models, schema
from sqlalchemy import text
from datetime import datetime ,timedelta


def create_rental(db: Session, rental: schema.RentalCreate):
    new_rental = models.Rental(**rental.model_dump())
    db.add(new_rental)
    db.commit()
    db.refresh(new_rental)
    return new_rental

def return_rental(db: Session,  rental: schema.RentalCreate,rental_id: int):
    rental = db.query(models.Rental).filter(models.Rental.rental_id == rental_id).first()
    if not rental:
        return None
    from datetime import datetime
    rental.return_date = datetime.now()
    db.commit()
    db.refresh(rental)
    return rental



def get_rental(db: Session, rental_id: int):
    return db.query(models.Rental).filter(models.Rental.rental_id == rental_id).first()

def get_all_rentals(db: Session,limit: int ,offset: int ):
    return db.query(models.Rental).limit(limit).offset(offset).all()

def get_overdue_rentals( db: Session):
    query = text("SELECT * FROM get_overdue_rentals(7)")
    result = db.execute(query).mappings().all()
    return result

def staff_performance(db:Session):
    query=text("select*from  staff_perform")
    result = db.execute(query).mappings().all()
    return result