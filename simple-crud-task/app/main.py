from fastapi import FastAPI
from app.core.database import Base, engine
from app.api.task import router as task_router

app = FastAPI(title="Task API")

@app.get("/")
def home():
    return {"message": "FastAPI is running inside and right in Docker!"}

@app.on_event("startup")
def init_db():
    Base.metadata.create_all(bind=engine)

app.include_router(task_router, prefix="/tasks", tags=["Tasks"])
