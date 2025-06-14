from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    clinic_name: str
    email: EmailStr
    password: str


class UserOut(BaseModel):
    id: int
    clinic_name: str
    email: EmailStr

    class Config:
        orm_mode = True
