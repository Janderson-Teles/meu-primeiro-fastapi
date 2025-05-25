from fastapi import APIRouter, HTTPException
from app.models import User

router = APIRouter()

@router.get("/")
def read_root():
    return {"message": "Bem-vindo à minha primeira API com FastAPI!"}

@router.post("/users/")
def create_user(user: User):
    return {"nome": user.nome, "email": user.email}