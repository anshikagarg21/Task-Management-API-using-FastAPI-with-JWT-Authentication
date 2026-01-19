from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, Token
from auth import hash_password, verify_password, create_access_token
from dependencies import get_db
 
router = APIRouter(prefix="/auth", tags=["Auth"])
 
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already exists")
 
    new_user = User(
        name=user.name,
        email=user.email,
        password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    return {"message": "User registered"}
 
@router.post("/login", response_model=Token)
def login(email: str, password: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
 
    token = create_access_token({"user_id": user.id})
    return {"access_token": token, "token_type": "bearer"}
 
 