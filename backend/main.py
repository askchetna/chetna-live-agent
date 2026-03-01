from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Chetna Live Backend")

class FounderInput(BaseModel):
    message: str

@app.get("/")
def health():
    return {"status": "Chetna Live Running"}

@app.post("/founder-command")
def founder_command(data: FounderInput):
    # Placeholder — Gemini Live integration will go here
    return {
        "received": data.message,
        "decision_draft": "Processing via Gemini Live..."
    }
