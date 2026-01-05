from app.repositories.task_repository import TaskRepository
from app.models.task import Task

repo = TaskRepository()

def list_tasks(db):
    return repo.get_all(db)

def create_task(db, data):
    task = Task(**data.dict())
    return repo.create(db, task)

def get_task(db, task_id):
    return repo.get(db, task_id)

def update_task(db, task, data):
    for key, value in data.dict(exclude_unset=True).items():
        setattr(task, key, value)
    repo.save(db)
    return task

def delete_task(db, task):
    repo.delete(db, task)
