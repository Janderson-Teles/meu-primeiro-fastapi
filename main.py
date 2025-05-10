from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class User(BaseModel):
    id: int
    nome: str
    email: str
    
usuarios_db: list[User] = []

@app.get("usuario")
def listar_usuarios():
    return usuarios_db

@app.get("/usuarios/{usuario_id}")
def buscar_usuario(usuario_id: int):
    for usuario in usuarios_db:
        return usuario
    raise HTTstPException(status_code=404, detail= "Usuário não encontrado")

@app.post("/usuarios")
def adicionar_usuario(usuario: User):
    usuarios_db.append(usuario)
    return {"mensagem": "USuário adicionado com sucesso"}
