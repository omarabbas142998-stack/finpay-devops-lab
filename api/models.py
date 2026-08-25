from sqlalchemy import Column, Integer, String, Numeric
from database import Base

class Account(Base):
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    owner = Column(String(100), nullable=False)
    balance = Column(Numeric(12, 2), nullable=False, default=0.00)
