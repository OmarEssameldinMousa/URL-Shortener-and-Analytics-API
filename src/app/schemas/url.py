from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime
import uuid


class URLCreate(BaseModel):
    original_url: HttpUrl = Field(..., description="The original URL to be shortened.")
    custom_slug: str | None = Field(None, min_length=3, max_length=50, description="Optional custom slug for the shortened URL.")
    ttl_seconds: int | None = Field(None, gt=0, description="Optional time-to-live for the shortened URL in seconds.")

class URLResponse(BaseModel):
    id: uuid.UUID
    original_url: str
    slug: str
    created_at: datetime
    expires_at: datetime | None

    class Config:
        from_attributes = True  # Allow Pydantic to read data from SQLAlchemy models using attribute access

        