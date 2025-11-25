from sqlalchemy import Column, Integer, String, DateTime
from database import Base
import datetime

class MoneyEntry(Base):
    __tablename__ = "MoneyEntry"  # or "money_entry" for convention
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer, nullable=False)
    category = Column(String, nullable=False)
    note = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
