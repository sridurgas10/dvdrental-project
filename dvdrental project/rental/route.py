from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbconnection import get_db
from . import crud, schema,models

rental_router = APIRouter(prefix="/rentals", tags=["Rentals"])

@rental_router.post("/", response_model=schema.RentalOut)
def create_rental(rental: schema.RentalCreate, db: Session = Depends(get_db)):
    return crud.create_rental(db, rental)

@rental_router.put("/return/{rental_id}", response_model=schema.RentalOut)
def return_rental(rental_id: int, rental: schema.RentalCreate,db: Session = Depends(get_db)):
    returned = crud.return_rental(db, rental,rental_id)
    if not returned:
        raise HTTPException(status_code=404, detail="Rental not found")
    return returned

@rental_router.get("/", response_model=schema.PaginatedRental)
def list_rentals(page:int,limit:int,db: Session = Depends(get_db)):
    offset=page*limit
    rental=crud.get_all_rentals(db,limit=limit, offset=offset)
    total = db.query(models.Rental).count()
    total_pages = (total + limit - 1) // limit

    return {
        "rental": rental,  
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "next_page": page + 1 if page < total_pages else None,
        "previous_page": page - 1 if page > 1 else None  
    }


@rental_router.get("/{rental_id}", response_model=schema.RentalOut)
def get_rental(rental_id: int, db: Session = Depends(get_db)):
    rental = crud.get_rental(db, rental_id)
    if not rental:
        raise HTTPException(status_code=404, detail="Rental not found")
    return rental

@rental_router.get("/overdue/", response_model=list[schema.OverdueRental])
def overdue_rentals( db: Session = Depends(get_db)):
    return crud.get_overdue_rentals(db)


@rental_router.get("/reports/staff_performance /",response_model=list[schema.StaffPerformance])
def staff_rental(db:Session=Depends(get_db)):
    return crud.staff_performance(db)