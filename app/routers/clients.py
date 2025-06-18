from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.schemas.client_schema import ClientCreate, ClientOut, ClientUpdate
from app.crud.client_crud import (
    create_client,
    get_clients,
    update_client,
    delete_client
)
from app.database import get_db
# from app.utils.auth import get_current_user
from app.models.user import User

router = APIRouter(
    tags=["Клиенты"]
)

@router.post("/", response_model=ClientOut)
def add_client(client: ClientCreate, db: Session = Depends(get_db)):
    # ВРЕМЕННО — user_id ставим вручную (например, 1)
    return create_client(db, client, user_id=1)

@router.get("/", response_model=List[ClientOut])
def list_clients(full_name: str = None, db: Session = Depends(get_db)):
    return get_clients(db, full_name=full_name)

@router.put("/{client_id}", response_model=ClientOut)
def edit_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)):
    return update_client(db, client_id, client)

@router.delete("/{client_id}")
def remove_client(client_id: int, db: Session = Depends(get_db)):
    delete_client(db, client_id)
    return {"detail": "Пациент удален"}
