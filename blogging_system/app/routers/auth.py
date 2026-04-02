from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.user import UserCreate, UserLogin
from app.models.user import User
from app.utils.hashing import hash_password, verify_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
         yield db
    finally:
        db.close()
        
@router.post("/register")
def register(user:UserCreate, db: Session = Depends(get_db)):
    new_user = User(
        email = user.email,
        password = hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"msg":"User Created!"}

@router.post("/login")
def login(user:UserLogin, db : Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
       return {
           "error":"User not found"
       } 
    if not verify_password(user.password, db_user.password):
        return {
            "error":"Wrong Creds"
        }
    return {
        "message":"User is Logged In successfully!"
    }