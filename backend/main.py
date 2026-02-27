from fastapi import FastAPI
from pydantic import BaseModel
from jejennorm import normalize_text
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class TextInput(BaseModel):
    text: str

@app.post("/normalize")
def normalize(input: TextInput):
    result = normalize_text(input.text)
    return {"normalized": result}

@app.get("/")
def root():
    return {"message": "Jejenorm backend running!"}