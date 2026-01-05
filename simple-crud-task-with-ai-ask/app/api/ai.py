from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
import os

router = APIRouter()

OLLAMA_HOST = os.getenv("OLLAMA_HOST", "ollama")
OLLAMA_PORT = os.getenv("OLLAMA_PORT", "11434")
OLLAMA_URL = f"http://{OLLAMA_HOST}:{OLLAMA_PORT}/api/generate"

class PromptRequest(BaseModel):
    prompt: str

@router.post("/ask")
def ai_ask(request: PromptRequest):
    payload = {
        "model": "mistral",
        "prompt": request.prompt,
        "max_tokens": 300,
        "stream": False
    }

    try:
        resp = requests.post(OLLAMA_URL, json=payload, timeout=120)
        resp.raise_for_status()

        data = resp.json()
        ai_text = data.get("response", "").strip()

        return {
            "status": "success",
            "ai_response": ai_text
        }

    except requests.exceptions.Timeout:
        raise HTTPException(
            status_code=504,
            detail="AI service timed out. Please try again."
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"AI service error: {str(e)}"
        )
