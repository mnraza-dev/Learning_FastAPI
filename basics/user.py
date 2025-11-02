from pydentic import BaseModel
from typing import Optional, List, Dict

class User(BaseModel):
    name: str
    age: int
    email: str
    married: bool = False
    skills: List[str]
    address: Optional[str] = None
    contact_details: Dict[str, str] 