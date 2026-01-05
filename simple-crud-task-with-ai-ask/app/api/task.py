from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.core.database import get_db
from app.services.task_service import (
    list_tasks, create_task, get_task, update_task, delete_task
)

router = APIRouter()

@router.get("/", response_model=list[TaskOut])
def get_tasks(db: Session = Depends(get_db)):
    return list_tasks(db)

@router.post("/", response_model=TaskOut, status_code=201)
def create(data: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, data)

@router.get("/{task_id}", response_model=TaskOut)
def retrieve(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return task

@router.patch("/{task_id}", response_model=TaskOut)
def update(task_id: int, data: TaskUpdate, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    return update_task(db, task, data)

@router.delete("/{task_id}")
def remove(task_id: int, db: Session = Depends(get_db)):
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(404, "Task not found")
    delete_task(db, task)
    return {"message": "Task deleted"}
