from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbconnection import get_db
from . import crud, schema,models

payment_router = APIRouter(prefix="/payments", tags=["Payments"])

@payment_router.post("/", response_model=schema.PaymentOut)
def create_payment(payment: schema.PaymentCreate, db: Session = Depends(get_db)):
    return crud.create_payment(db, payment)

@payment_router.get("/{payment_id}", response_model=schema.PaymentOut)
def get_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = crud.get_payment(db, payment_id)
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

@payment_router.get("/", response_model=schema.PaginatedPayment)
def list_payments(page: int , limit: int , db: Session = Depends(get_db)):
    offset = page  * limit
    payment = crud.get_all_payments(db, limit, offset)  

    total = db.query(models.Payment).count()
    total_pages = (total + limit - 1) // limit

    return {
        "payment": payment,  
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "next_page": page + 1 if page < total_pages else None,
        "previous_page": page - 1 if page > 1 else None  
    }


@payment_router.get("/customer/{customer_id}", response_model=list[schema.PaymentOut])
def customer_payments(customer_id: int, db: Session = Depends(get_db)):
    return crud.get_customer_payments(db, customer_id)
