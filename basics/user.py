from pydentic import BaseModel,EmailStr, AnyUrl
from typing import Optional, List, Dict, Annotated

class User(BaseModel):
    name: Annotated[str, Field(max_length=50, title="Full Name", description="The user's full name cannot exceed 50 characters", example="Jane Doe")]
    age: int = Field(..., gt=0, strict=True, description="Age must be a positive integer")
    portfolio: Optional[AnyUrl] = None
    email: EmailStr
    married: bool = False
    skills: List[str] = Field(max_length=5)
    address: Optional[str] = None
    contact_details: Dict[str, str] 