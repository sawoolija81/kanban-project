from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime, timezone 
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(String, default='user')
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))