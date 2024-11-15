from main import app
from classes import Usuario
from fastapi import Query

@app.get("/usuarios/listar")
def lista_usuarios():
    return {
        "usuarios": dict()
    }
    
@app.post("/usuarios/criar")
def cria_usuario(usuario: Usuario):
    return {
        
    }
    
@app.put("/usuarios/editar/{id}")
def edita_usuario(id: int):
    return {
        
    }
    
@app.delete("/usuarios/deletar/{id}")
def deleta_usuario(id: int):
    return {
        
    }