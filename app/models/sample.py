from pydantic import BaseModel
from typing import Optional

class SampleModel(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    is_active: bool = True

    class Config:
        from_attributes = True 