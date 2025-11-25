from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func
from database import engine, SessionLocal, Base
from models import MoneyEntry
from pydantic import BaseModel

app = FastAPI(title="Expense Tracker Backend")
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------- DB Dependency -----------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------- Pydantic Schema -----------------
class MoneyInput(BaseModel):
    category: str
    amount: int
    note: str

class FriendExpenseInput(BaseModel):
    friend_name: str
    amount: int
    note: str | None = None 

# ----------------- ADD ENTRY -----------------
@app.post("/add", tags=["Add your Expense"])
def add_expense(payload: MoneyInput, db: Session = Depends(get_db)):
    try:
        new_entry = MoneyEntry(
            category=payload.category,
            amount=payload.amount,
            note=payload.note
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)

        return {
            "message": f"Created entry for {payload.category}",
            "id": new_entry.id,
            "category": new_entry.category,
            "amount": new_entry.amount,
            "note": new_entry.note
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ----------------- TOTAL SPENDING -----------------
@app.get("/total", tags=["Total Expense"])
def get_total_spending(db: Session = Depends(get_db)):
    total = db.query(func.sum(MoneyEntry.amount)).scalar()
    return {"total_spending": total or 0}

# ----------------- GET ALL ENTRIES (with optional category filter) -----------------
@app.get("/entries", tags=["Retrieve All Entries"])
def get_all_entries(
    category: str | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(MoneyEntry)

    if category:
        query = query.filter(MoneyEntry.category == category)

    entries = query.order_by(MoneyEntry.id.desc()).all()

    return [
        {
            "id": e.id,
            "category": e.category,
            "amount": e.amount,
            "note": e.note
        }
        for e in entries
    ]

# ----------------- GET SINGLE ENTRY -----------------
@app.get("/entry/{id}", tags=["Retrieve Single Entry"])
def get_entry(id: int, db: Session = Depends(get_db)):
    entry = db.query(MoneyEntry).filter(MoneyEntry.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    return {
        "id": entry.id,
        "category": entry.category,
        "amount": entry.amount,
        "note": entry.note
    }

# ----------------- DELETE ENTRY -----------------
@app.delete("/entry/{id}", tags=["Delete Entry"])
def delete_entry(id: int, db: Session = Depends(get_db)):
    entry = db.query(MoneyEntry).filter(MoneyEntry.id == id).first()

    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    db.delete(entry)
    db.commit()
    return {"message": "Entry deleted successfully"}

@app.post("/give", tags=["Friend Expenses"])
def give_cash(payload: FriendExpenseInput, db: Session = Depends(get_db)):
    try:
        # Store as a MoneyEntry with category = "Friend"
        note_text = f"Gave ₹{payload.amount} to {payload.friend_name}"
        if payload.note:
            note_text += f" ({payload.note})"

        new_entry = MoneyEntry(
            category="Friend",
            amount=payload.amount,
            note=note_text
        )
        db.add(new_entry)
        db.commit()
        db.refresh(new_entry)

        return {
            "message": f"Recorded cash given to {payload.friend_name}",
            "id": new_entry.id,
            "category": new_entry.category,
            "amount": new_entry.amount,
            "note": new_entry.note
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
