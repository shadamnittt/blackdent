from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    clinic_name: str
    email: EmailStr
    password: str
    username: Optional[str]


class UserOut(BaseModel):
    id: int
    clinic_name: str
    email: EmailStr
    username: Optional[str]

    class Config:
        orm_mode = True
