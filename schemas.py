from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
 
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
 
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
 
    class Config:
        orm_mode = True
 
class Token(BaseModel):
    access_token: str
    token_type: str
 
class TaskCreate(BaseModel):
    title: str
    description: str
    priority: str
    due_date: datetime
 
class TaskUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    status: Optional[str]
    priority: Optional[str]
 
 