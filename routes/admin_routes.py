from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import User
from dependencies import get_db, get_current_user
 
router = APIRouter(prefix="/admin", tags=["Admin"])
 
@router.get("/users")
def get_users(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user.role != "admin":
        raise HTTPException(status_code=403)
    return db.query(User).all()
 
 