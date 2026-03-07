import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, func, URL
from app.core.database import Base
from .enums.enums import TableNames

class User(Base):
    __tablename__ = TableNames.USERS.value

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)

    api_key_hash: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    
    # Use standard python datetime in the type hint
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationship to URLs
    urls: Mapped[list["URL"]] = relationship(
        "URL", 
        back_populates="user", 
        cascade="all, delete-orphan", 
    )