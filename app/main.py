from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal, engine
from app.models import Base, Lead
from app.schemas import LeadCreate, LeadOut
from app.services.api_client import fetch_city_info


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/api/leads", response_model=LeadOut)
async def create_lead(lead: LeadCreate, db: Session = Depends(get_db)):
    
    # 1. Llamar API externa 
    external_info = await fetch_city_info(lead.city)
    print("INFO DE API EXTERNA:", external_info)

    # 2. Crear objeto ORM
    db_lead = Lead(
        name=lead.name,
        city=lead.city,
        phone=lead.phone,
        address=lead.address
        
    )

    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)

    return db_lead

@app.get("/api/leads", response_model=list[LeadOut])
def list_leads(db: Session = Depends(get_db)):
    return db.query(Lead).all()

@app.get("/api/leads/similar")
def similar(name: str, db: Session = Depends(get_db)):
    return db.query(Lead).filter(Lead.name.ilike(f"%{name}%")).all()

