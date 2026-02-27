from fastapi import FastAPI
from pydantic import BaseModel
from jejennorm import normalize_text, detect_sentiment, load_dataset
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

# Load the Filipino slang dataset at startup
ngram_rules = load_dataset()

class TextInput(BaseModel):
    text: str

@app.post("/normalize")
def normalize(input: TextInput):
    normalized = normalize_text(input.text, ngram_rules)
    sentiment = detect_sentiment(input.text)
    return {
        "normalized": normalized,
        "sentiment": sentiment,
        "original_length": len(input.text),
        "normalized_length": len(normalized)
    }

@app.get("/")
def root():
    return {"message": "Jejenorm backend running!"}