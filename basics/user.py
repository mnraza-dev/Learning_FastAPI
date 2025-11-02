from pydentic import BaseModel,EmailStr, AnyUrl
from typing import Optional, List, Dict

class User(BaseModel):
    name: str
    age: int
    portfolio: Optional[AnyUrl] = None
    email: EmailStr
    married: bool = False
    skills: List[str]
    address: Optional[str] = None
    contact_details: Dict[str, str] 