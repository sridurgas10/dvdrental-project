from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from auth import models, auth, schema
from dbconnection import get_db
from datetime import datetime
from sqlalchemy import text

router = APIRouter()

@router.post("/auth/signup", response_model=schema.StaffOut)
def signup(user: schema.StaffCreate, db: Session = Depends(get_db)):


    existing = db.query(models.StaffUser).filter(models.StaffUser.username == user.username).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = auth.pwd_context.hash(user.password)
    new_user = models.StaffUser(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user



@router.post("/auth/login", response_model=schema.Token)
def login(user: schema.StaffLogin, db: Session = Depends(get_db)):

    db_user = db.query(models.StaffUser).filter( models.StaffUser.username == user.username).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid username or password")

    token = auth.create_token(db_user.username,db_user.email)

    return {"access_token": token, "token_type": "bearer"}



@router.get("/auth/me", response_model=schema.StaffOut)
def get_me(token: schema.StaffMe, db: Session = Depends(get_db)):

    username = auth.verify_token(token)

    user = db.query(models.StaffUser).filter(models.StaffUser.username == username).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

