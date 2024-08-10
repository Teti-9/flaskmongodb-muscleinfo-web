from pydantic import ConfigDict, BaseModel
from typing import Optional

class Exercicios(BaseModel):
    nome: str
    musculo: str
    info: str
    dicas: str
    model_config = ConfigDict(from_attributes=True)