from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class EndingBase(BaseModel):
    work: str
    query: str

class EndingCreate(EndingBase):
    pass

class EndingUpdate(EndingBase):
    work: Optional[str] = None
    query: Optional[str] = None
    content: Optional[str] = None

class EndingInDB(EndingBase):
    id: int
    content: str
    user_id: int
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True 