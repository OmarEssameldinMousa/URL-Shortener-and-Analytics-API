import uuid
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import URL, String, DateTime, func, ForeignKey
from app.core.database import Base
from .enums.enums import TableNames

class ClickEvent(Base):
    __tablename__ = TableNames.CLICK_EVENTS.value

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    
    # CORRECT FOREIGN KEY USAGE:
    url_id: Mapped[uuid.UUID] = mapped_column(ForeignKey(f"{TableNames.URLS.value}.id", ondelete="CASCADE"), nullable=False)
    
    # Note the `str | None` because nullable=True
    ip_address: Mapped[str | None] = mapped_column(String(45), nullable=True)
    country: Mapped[str | None] = mapped_column(String(100), nullable=True)
    
    # ADDED missing user_agent
    user_agent: Mapped[str | None] = mapped_column(String(512), nullable=True)
    
    clicked_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    # Relationship back to URL
    url: Mapped["URL"] = relationship("URL", back_populates="clicks")