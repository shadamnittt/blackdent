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

router = APIRouter(
    prefix="/clients",
    tags=["Клиенты"]
)

@router.post("/", response_model=ClientOut)
def add_client(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db, client)

@router.get("/", response_model=List[ClientOut])
def list_clients(
    db: Session = Depends(get_db),
    full_name: Optional[str] = Query(None),
    status: Optional[str] = Query(None),
    date_created: Optional[str] = Query(None),
):
    return get_clients(db, full_name, status, date_created)

@router.put("/{client_id}", response_model=ClientOut)
def edit_client(client_id: int, client: ClientUpdate, db: Session = Depends(get_db)):
    return update_client(db, client_id, client)

@router.delete("/{client_id}")
def remove_client(client_id: int, db: Session = Depends(get_db)):
    delete_client(db, client_id)
    return {"detail": "Пациент удален"}
