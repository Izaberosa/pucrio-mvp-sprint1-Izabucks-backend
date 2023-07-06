from unicodedata import category
from pydantic import BaseModel
from typing import Optional, List
from model.bebida import Bebida


class BebidaSchema(BaseModel):
    nome: str = "Pink Drink"
    descricao: Optional[str] = "Uma bebida de Morango com adição de leite, castanha de caju, batidos com gelos na coqueteleira"
    categoria: str = "Refresher"
    imagem: str = "https://i.pinimg.com/564x/08/4b/5e/084b5ee52776b58afb3d138b0d0c5693.jpg"
    valor: float = 16.80


class BebidaBuscaSchema(BaseModel):
    id: Optional[int] = 1
    nome: Optional[str] = "Pink Drink"


class BebidaViewSchema(BaseModel):
    id: int = 1
    nome: str = "Pink Drink"
    descricao: Optional[str] = "Uma bebida de Morango com adição de leite, castanha de caju, batidos com gelos na coqueteleira"
    categoria: str = "Refresher"
    imagem: str = "https://i.pinimg.com/564x/08/4b/5e/084b5ee52776b58afb3d138b0d0c5693.jpg"
    valor: float = 16.80
    total_cometarios: int = 1
    nota_media: int = 0


class BebidaDelSchema(BaseModel):
    mesage: str
    id: int

def apresenta_bebida(bebida):
    nota_media = 0
     
    return {
        "id": bebida.id,
        "nome": bebida.nome,
        "categoria": bebida.categoria,
        "descricao": bebida.descricao,
        "imagem": bebida.imagem_path,
        "valor": bebida.valor,
        "price": bebida.valor,
        "nota_media": nota_media,
    }


class BebidaListaViewSchema(BaseModel):
    bebidas: List[BebidaViewSchema]


def apresenta_bebidas(bebidas:List[Bebida]):
    result = []
    for bebida in bebidas:
        result.append({ 
        "id": bebida.id,
        "nome": bebida.nome,
        "categoria": bebida.categoria,
        "descricao": bebida.descricao,
        "imagem": bebida.imagem_path,
        "valor": bebida.valor,
        "price": bebida.valor,
        })
    return {"bebidas": result}
