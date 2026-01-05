from sqlalchemy.orm import Session
from sqlalchemy import select
from app.models.task import Task

class TaskRepository:

    def get_all(self, db: Session):
        return db.scalars(select(Task)).all()

    def create(self, db: Session, task: Task):
        db.add(task)
        db.commit()
        db.refresh(task)
        return task

    def get(self, db: Session, task_id: int):
        return db.get(Task, task_id)

    def delete(self, db: Session, task):
        db.delete(task)
        db.commit()

    def save(self, db: Session):
        db.commit()
