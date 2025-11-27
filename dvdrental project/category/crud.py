from sqlalchemy.orm import Session
from . import model, schema
from sqlalchemy import text

def get_all_category(db: Session,limit: int ,offset: int ):
    return db.query(model.Category).limit(limit).offset(offset).all()

def get_category(db: Session, category_id: int):
    return db.query(model.Category).filter(model.Category.category_id == category_id).first()

def create_category(db: Session, category: schema.CategoryCreate):
    new_category = model.Category(**category.model_dump())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

def update_category(db: Session, category_id: int, category: schema.CategoryCreate):
    db_category = db.query(model.Category).filter(model.Category.category_id == category_id).first()
    if not db_category:
        return None
    for key, value in category.model_dump().items():
        setattr(db_category, key, value)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category= db.query(model.Category).filter(model.Category.category_id == category_id).first()
    if not db_category:
        return None
    db.delete(db_category)
    db.commit()
    return db_category