from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    login: str
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    login: str
    email: EmailStr
    role: str
    created_at: datetime
    
    class Config:
        from_attributes = True