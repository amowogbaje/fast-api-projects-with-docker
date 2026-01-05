# Simple Task CRUD

A FastAPI project implementing a CRUD API for tasks.

---

## Features

- Create, Read, Update, Delete tasks
- PostgreSQL database support
- Dockerized backend
- Pydantic models for request validation
- Swagger / OpenAPI documentation

---

## Requirements

- Docker & Docker Compose

## Setup

1. since this project is automatically cloned with the parent folder

2. Create a .env file:

```
    FASTAPI_PORT=4001
    DB_HOST=postgres
    DB_PORT=5432
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_NAME=tasks_db
```

3. Build and start containers:

``` docker compose up --build -d ```

4. Access API docs:

``` http://localhost:4001/docs ```


## ENDPOINTS

| Method | Endpoint      | Description    | Request Body                                                                                            |
| ------ | ------------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| GET    | `/tasks/`     | List all tasks | –                                                                                                       |
| POST   | `/tasks/`     | Create a task  | `{ "title": "string", "description": "string (optional)", "status": true/false (optional) }`            |
| GET    | `/tasks/{id}` | Get a task     | –                                                                                                       |
| PATCH  | `/tasks/{id}` | Update a task  | `{ "title": "string (optional)", "description": "string (optional)", "status": true/false (optional) }` |
| DELETE | `/tasks/{id}` | Delete a task  | –                                                                                                       |
