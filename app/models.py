from sqlalchemy import Column, Integer, String
from app.db import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    city = Column(String)
    phone = Column(String)
    address = Column(String)
