# Simple Task CRUD with AI

Extends the simple task CRUD API by integrating AI-powered task suggestions.

---

## Features

- All features from simple-crud-task
- AI integration via Ollama (local) or hosted LLMs
- `/ai/ask` endpoint for generating task suggestions
- Dockerized backend with AI service container
- Human-readable AI responses (`status` + `ai_response`)
- Pydantic validation and structured API responses
- OpenAPI / Swagger docs at `/docs`

---

## Requirements

- Docker & Docker Compose
- Python 3.12
- Optional: Ollama container or API key for hosted LLM

---

## Setup

1. Navigate to this folder:

2. Create a .env file:

```
    FASTAPI_PORT=4002
    DB_HOST=postgres
    DB_PORT=5432
    DB_USER=postgres
    DB_PASSWORD=postgres
    DB_NAME=tasks_db

    OLLAMA_HOST=ollama        # or hosted LLM endpoint
    OLLAMA_PORT=11434
```

3. Build and start containers:

``` 
docker compose up --build -d 

```

4. Access API docs:

``` 
http://localhost:4002/docs 

```



## ENDPOINTS

### Tasks (same as simple-crud-task)

| Method | Endpoint      | Description    | Request Body                                                                                            |
| ------ | ------------- | -------------- | ------------------------------------------------------------------------------------------------------- |
| GET    | `/tasks/`     | List all tasks | –                                                                                                       |
| POST   | `/tasks/`     | Create a task  | `{ "title": "string", "description": "string (optional)", "status": true/false (optional) }`            |
| GET    | `/tasks/{id}` | Get a task     | –                                                                                                       |
| PATCH  | `/tasks/{id}` | Update a task  | `{ "title": "string (optional)", "description": "string (optional)", "status": true/false (optional) }` |
| DELETE | `/tasks/{id}` | Delete a task  | –                                                                                


### AI

| Method | Endpoint  | Description                                  | Request Body             |
| ------ | --------- | -------------------------------------------- | ------------------------ |
| POST   | `/ai/ask` | Ask the AI for task suggestions or responses | `{ "prompt": "string" }` |

- prompt is a string containing the question or instruction for the AI.