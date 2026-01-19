from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Task
from schemas import TaskCreate, TaskUpdate
from dependencies import get_db, get_current_user
 
router = APIRouter(prefix="/tasks", tags=["Tasks"])
 
@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    new_task = Task(**task.dict(), created_by=user.id)
    db.add(new_task)
    db.commit()
    return {"message": "Task created"}
 
@router.get("/")
def get_tasks(db: Session = Depends(get_db), user=Depends(get_current_user)):
    if user.role == "admin":
        return db.query(Task).all()
    return db.query(Task).filter(Task.created_by == user.id).all()
 
@router.put("/{task_id}")
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    t = db.query(Task).filter(Task.id == task_id).first()
    if not t:
        raise HTTPException(status_code=404)
 
    if user.role != "admin" and t.created_by != user.id:
        raise HTTPException(status_code=403)
 
    for key, value in task.dict(exclude_unset=True).items():
        setattr(t, key, value)
 
    db.commit()
    return {"message": "Task updated"}
 
@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404)
 
    if user.role != "admin" and task.created_by != user.id:
        raise HTTPException(status_code=403)
 
    db.delete(task)
    db.commit()
    return {"message": "Task deleted"}
 
 