from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import create_user
from app.dependencies import get_db

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = create_user(db=db, user=user)
    if not db_user:
        raise HTTPException(status_code=400, detail="User registration failed.")
    return db_user



