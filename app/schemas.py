from pydantic import BaseModel

class LeadCreate(BaseModel):
    name: str
    city: str
    phone: str
    address: str | None = None

class LeadOut(LeadCreate):
    id: int

    class Config:
        from_attributes = True  # Reemplazo de orm_mode



