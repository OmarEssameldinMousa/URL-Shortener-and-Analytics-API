import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, func, ForeignKey
from app.core.database import Base
from .enums.enums import TableNames

class URL(Base):
    __tablename__ = TableNames.URLS.value

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    original_url: Mapped[str] = mapped_column(String(2048), nullable=False)
    slug: Mapped[str] = mapped_column(String(255), unique=True, index=True, nullable=False)
    
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    
    # Note the `datetime | None` because nullable=True
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    
    # CORRECT FOREIGN KEY USAGE:
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(f"{TableNames.USERS.value}.id", ondelete="CASCADE"), nullable=False)

    # Relationship back to User
    user: Mapped["User"] = relationship("User", back_populates="urls")
    
    # Relationship to ClickEvents
    clicks: Mapped[list["ClickEvent"]] = relationship(
        "ClickEvent", 
        back_populates="url", 
        cascade="all, delete-orphan"
    )