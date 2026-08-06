from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas import UserCreate, UserResponse
from app.security import hash_password

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Kanban API работает"}


@app.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(
        (User.login == user.login) | (User.email == user.email)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail = "Login или email уже заняты")  


    hashed = hash_password(user.password)

    new_user = User(
        login = user.login,
        email=user.email,
        hashed_password=hashed,
    )


    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user