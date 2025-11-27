from sqlalchemy.orm import Session
from . import models, schema
from sqlalchemy import text

def get_all_customers(db: Session,limit: int ,offset: int ):
    return db.query(models.Customer).limit(limit).offset(offset).all()

def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()

def create_customer(db: Session, customer: schema.CustomerCreate):
    new_customer = models.Customer(**customer.model_dump())
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    return new_customer

def update_customer(db: Session, customer_id: int, customer: schema.CustomerCreate):
    db_customer = db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()
    if not db_customer:
        return None
    for key, value in customer.model_dump().items():
        setattr(db_customer, key, value)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def delete_customer(db: Session, customer_id: int):
    db_customer = db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()
    if not db_customer:
        return None
    db.delete(db_customer)
    db.commit()
    return db_customer

def customer_rental(db:Session):
    query=text("select *from customer_rental_history")
    result=db.execute(query).mappings().all()
    return result

def customer_rental(customer_id: int, db: Session):
    query = text("SELECT calculate_total_rental_cost(:cid)")
    result = db.execute(query, {"cid": customer_id}).scalar()
    return result

def top_customer(db:Session):
    query=text("select*from top5_customer")
    result=db.execute(query).mappings().all()
    return result