import uvicorn
from fastapi import FastAPI
from mocks import mocked_usuario

app = FastAPI()

@app.get("/")
def home():
    return {
        "mensagem": "Hello, world!"
    }

@app.get("/usuario/listar")
def lista_usuario():
    return {
        "code": 200,
        "usuarios": mocked_usuario
    }
    
@app.get("/usuario/{id}")
def lista_por_id(id: int):
    return mocked_usuario[id]

    
@app.get("/livros/listar")
def lista_usuario():
    return {
        "code": 200,
        "quantidade_usuarios": len(mocked_usuario),
        "usuarios": mocked_usuario
    }

# @app.put("/usuarios/editar/{id}")
# def edita(id):
#     edita_usuarios(id)

# @app.delete("/usuarios/deletar/{id}")
# def deleta(id): 
#     deleta_usuarios(id)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)