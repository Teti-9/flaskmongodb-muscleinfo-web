from src.infra.mongodb.config.database import collection_name
from src.routers.utils import list_serial
import re

class RepositorioExercicios:

    def __init__(self):
        pass

    def criar_estrutura(template):
        collection_name.insert_one(template.dict())
    
    def procurar_musculo(musculo: str):
        regex_pattern = re.compile(musculo, re.IGNORECASE)
        exercicios = list_serial(collection_name.find({"musculo": {"$regex": regex_pattern}}))
        return exercicios
    
    def editar_musculo(nome: str, info):
        collection_name.find_one_and_update({"nome": nome}, {"$set": {'info': info}})

    def deletar_musculo(nome: str):
        collection_name.find_one_and_delete({"nome": nome})

    def procurar_exercicio(nome: str):
        exercicio = collection_name.find_one({"nome": nome})
        return exercicio