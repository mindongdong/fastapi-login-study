
from typing import List, Optional
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: Optional[EmailStr] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
