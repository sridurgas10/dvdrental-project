from sqlalchemy.orm import Session
from . import models, schema

def create_payment(db: Session, payment: schema.PaymentCreate):
    new_payment = models.Payment(**payment.model_dump())
    db.add(new_payment)
    db.commit()
    db.refresh(new_payment)
    return new_payment

def get_payment(db: Session, payment_id: int):
    return db.query(models.Payment).filter(models.Payment.payment_id == payment_id).first()

def get_all_payments(db: Session,limit: int ,offset: int ):
    return db.query(models.Payment).limit(limit).offset(offset).all()

def get_customer_payments(db: Session, customer_id: int):
    return db.query(models.Payment).filter(models.Payment.customer_id == customer_id).all()
