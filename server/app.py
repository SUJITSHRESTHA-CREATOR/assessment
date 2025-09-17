from fastapi import FastAPI, Request
from pydantic import BaseModel
import sqlite3, json, time
from db import init_db, insert_record
from bs4 import BeautifulSoup
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# initialize DB
init_db()

class IngestRequest(BaseModel):
    url: str
    html: str
    instruction: str

@app.post("/ingest")
async def ingest(req: IngestRequest):
    # Parse fields (
    fields = [f.strip().lower() for f in req.instruction.replace("and", ",").split(",") if f.strip()]

    # Extract 
    soup = BeautifulSoup(req.html, "html.parser")
    
    for tag in soup(["script", "style"]):
        tag.decompose()
        
    extracted, confidence = {}, {}

    if "title" in fields:
        title = soup.title.string.strip() if soup.title else None
        extracted["title"] = title
        confidence["title"] = 0.9 if title else 0.2

    if "price" in fields:
        price_tag = soup.find(class_=lambda c: c and "price" in c.lower())
        if not price_tag:
            price_tag = soup.find(string=lambda text: text and "$" in text)
        extracted["price"] = price_tag.get_text(strip=True) if price_tag else None
        confidence["price"] = 0.9 if price_tag else 0.2

    if "rating" in fields:
        rating_tag = soup.find(string=lambda text: text and "out of 5" in text)
        extracted["rating"] = rating_tag.strip() if rating_tag else None
        confidence["rating"] = 0.6 if rating_tag else 0.2

    record_id = f"rec_{int(time.time())}"

    # Save in DB
    insert_record(record_id, req.url, req.instruction, fields, extracted, confidence)

    return {
        "url": req.url,
        "instruction": req.instruction,
        "parsed_fields": fields,
        "extracted": extracted,
        "confidence": confidence,
        "record_id": record_id
    }
