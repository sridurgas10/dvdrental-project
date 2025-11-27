from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbconnection import get_db
from . import crud, schema,models

customer_router = APIRouter(prefix="/customers", tags=["Customers"])

@customer_router.get("/", response_model=schema.PaginatedCustomer)
def list_customers(page:int,limit:int,db: Session = Depends(get_db)):
    offset=page*limit
    customers= crud.get_all_customers(db,limit=limit, offset=offset)
    total = db.query(models.Customer).count()
    total_pages = (total + limit - 1) // limit

    return {
        "customers": customers,  
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "next_page": page + 1 if page < total_pages else None,
        "previous_page": page - 1 if page > 1 else None  
    }


@customer_router.get("/{customer_id}", response_model=schema.CustomerOut)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    customer = crud.get_customer(db, customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer

@customer_router.post("/", response_model=schema.CustomerOut)
def create_customer(customer: schema.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@customer_router.put("/{customer_id}", response_model=schema.CustomerOut)
def update_customer(customer_id: int, customer: schema.CustomerCreate, db: Session = Depends(get_db)):
    updated_customer = crud.update_customer(db, customer_id, customer)
    if not updated_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer

@customer_router.delete("/{customer_id}", response_model=schema.CustomerOut)
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    deleted_customer = crud.delete_customer(db, customer_id)
    if not deleted_customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return deleted_customer

@customer_router.get("/reports/customer_rental_view/",response_model=list[schema.CustomerRental])
def customer_rental_view(db:Session=Depends(get_db)):
    return crud.customer_rental(db)

@customer_router.get("/analytics/customer/{customer_id}/total_spend/",response_model=schema. RentalCost)
def customer_rental_view(customer_id:int,db:Session=Depends(get_db)):
    cost=crud.customer_rental(customer_id,db)
    return {"customer_id": customer_id, "total_rental_cost": cost}


@customer_router.get("/reports/top_customers/",response_model=list[schema.TopCustomer])
def rental_customer(db:Session=Depends(get_db)):
    return crud.top_customer(db)

