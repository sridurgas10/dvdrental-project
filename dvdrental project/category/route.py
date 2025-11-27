from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dbconnection import get_db
from . import crud, schema,model

category_router = APIRouter(prefix="/category", tags=["Category"])

@category_router.get("/", response_model=schema.PaginatedCategory)
def list_category(page:int,limit:int,db: Session = Depends(get_db)):
    offset=page*limit
    category= crud.get_all_category(db, limit=limit, offset=offset)
    total = db.query(model.Category).count()
    total_pages = (total + limit - 1) // limit

    return {
        "category": category,  
        "page": page,
        "limit": limit,
        "total_pages": total_pages,
        "next_page": page + 1 if page < total_pages else None,
        "previous_page": page - 1 if page > 1 else None  
    }


@category_router.get("/{category_id}", response_model=schema.CategoryOut)
def get_category(category_id: int, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@category_router.post("/", response_model=schema.CategoryOut)
def create_category(category: schema.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@category_router.put("/{category_id}", response_model=schema.CategoryOut)
def update_category(category_id: int, category: schema.CategoryCreate, db: Session = Depends(get_db)):
    updated_category = crud.update_category(db, category_id, category)
    if not updated_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return updated_category

@category_router.delete("/{category_id}", response_model=schema.CategoryOut)
def delete_customer(category_id: int, db: Session = Depends(get_db)):
    deleted_category = crud.delete_category(db, category_id)
    if not deleted_category:
        raise HTTPException(status_code=404, detail="Category not found")
    return deleted_category
