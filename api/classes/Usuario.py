from pydantic import BaseModel
from datetime import date

class Usuario_Modelo(BaseModel):
    nome: str
    sobrenome: str
    email: str
    documento: str | None = None
    ativo: bool
    data_de_criacao: date