from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client_schema import ClientCreate, ClientUpdate
from datetime import datetime

# Добавить клиента
def create_client(db: Session, client: ClientCreate, user_id: int):
    db_client = Client(
        full_name=client.full_name,
        phone_number=client.phone_number,
        status=client.status,
        comment=client.comment,
        date_created=datetime.utcnow(),
        user_id=user_id
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session, full_name: str = None, skip: int = 0, limit: int = 100):
    query = db.query(Client)
    if full_name:
        query = query.filter(Client.full_name.ilike(f"%{full_name}%"))
    return query.offset(skip).limit(limit).all()

# Обновить клиента
def update_client(db: Session, client_id: int, client: ClientUpdate):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if not db_client:
        return None
    for key, value in client.dict().items():
        setattr(db_client, key, value)
    db.commit()
    db.refresh(db_client)
    return db_client

# Удалить клиента
def delete_client(db: Session, client_id: int):
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if not db_client:
        return None
    db.delete(db_client)
    db.commit()
    return db_client
