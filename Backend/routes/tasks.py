from typing import List, Optional
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from sqlmodel import Session, select

from models import Task, User
from db import get_session
from auth import get_current_user


class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.post("/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    new_task = Task(**task.model_dump(), user_id=current_user.id)
    session.add(new_task)
    session.commit()
    session.refresh(new_task)
    return new_task

@router.get("/", response_model=List[Task])
def read_tasks(
    current_user: User = Depends(get_current_user), 
    session: Session = Depends(get_session),
    status: Optional[str] = None,
    sort: Optional[str] = None,
):
    query = select(Task).where(Task.user_id == current_user.id)
    
    if status == "pending":
        query = query.where(Task.completed == False)
    elif status == "completed":
        query = query.where(Task.completed == True)

    if sort == "title":
        query = query.order_by(Task.title)
    elif sort == "updated":
        query = query.order_by(Task.updated_at.desc())
    else: # "created" or default
        query = query.order_by(Task.created_at.desc())

    tasks = session.exec(query).all()
    return tasks

@router.get("/{id}", response_model=Task)
def read_task(id: int, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    task = session.exec(select(Task).where(Task.id == id, Task.user_id == current_user.id)).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
    return task

@router.put("/{id}", response_model=Task)
def update_task(id: int, task: TaskUpdate, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    db_task = session.exec(select(Task).where(Task.id == id, Task.user_id == current_user.id)).first()
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found or not authorized")
    
    task_data = task.model_dump(exclude_unset=True)
    for key, value in task_data.items():
        setattr(db_task, key, value)
    
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(id: int, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    task = session.exec(select(Task).where(Task.id == id, Task.user_id == current_user.id)).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found or not authorized")
    session.delete(task)
    session.commit()
    return {"message": "Task deleted successfully"}

class TaskCompletion(BaseModel):
    completed: bool

@router.patch("/{id}/complete", response_model=Task)
def toggle_task_completion(id: int, task_completion: TaskCompletion, current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    db_task = session.exec(select(Task).where(Task.id == id, Task.user_id == current_user.id)).first()
    if not db_task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found or not authorized")
    
    db_task.completed = task_completion.completed
    
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task