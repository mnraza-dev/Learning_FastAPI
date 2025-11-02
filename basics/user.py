from pydentic import BaseModel,EmailStr, AnyUrl
from typing import Optional, List, Dict

class User(BaseModel):
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., gt=0, description="Age must be a positive integer")
    portfolio: Optional[AnyUrl] = None
    email: EmailStr
    married: bool = False
    skills: List[str] = Field(max_length=5)
    address: Optional[str] = None
    contact_details: Dict[str, str] 