from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.schemas import user as user_schema
from app.models import user as user_model
from app.utils import auth, deps  
from app.database import get_db

router = APIRouter()

@router.post("/register", response_model=user_schema.UserOut)
def register(user_data: user_schema.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(user_model.User).filter(user_model.User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email уже зарегистрирован")
    
    new_user = user_model.User(
        clinic_name=user_data.clinic_name,
        email=user_data.email,
        password_hash=auth.hash_password(user_data.password),
        username=user_data.username
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(user_model.User).filter(user_model.User.email == form_data.username).first()
    if not user or not auth.verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Неверный email или пароль")
    
    access_token = auth.create_access_token({"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me", response_model=user_schema.UserOut)
def get_current_user(current_user: user_model.User = Depends(deps.get_current_user)):  
    return current_user
