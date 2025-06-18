from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Базовая схема (для создания и редактирования)
class ClientBase(BaseModel):
    full_name: str
    phone_number: str
    status: str  # "надежный", "проблемный"
    comment: Optional[str] = None

# Схема для создания пациента
class ClientCreate(ClientBase):
    pass

# Схема для обновления пациента
class ClientUpdate(ClientBase):
    pass

# Схема для ответа клиенту
class ClientOut(BaseModel):
    id: int
    full_name: str
    phone_number: str
    status: str
    comment: str
    date_created: datetime

    class Config:
        from_attributes = True

