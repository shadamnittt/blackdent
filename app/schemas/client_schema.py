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
class ClientOut(ClientBase):
    id: int
    date_created: datetime
    user_id: int

    class Config:
        orm_mode = True
