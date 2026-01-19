from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime
 
class User(Base):
    __tablename__ = "users"
 
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="user")
 
    tasks = relationship("Task", back_populates="creator")
 
 
class Task(Base):
    __tablename__ = "tasks"
 
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    status = Column(String, default="pending")
    priority = Column(String)
    due_date = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
 
    created_by = Column(Integer, ForeignKey("users.id"))
    creator = relationship("User", back_populates="tasks")
 
 