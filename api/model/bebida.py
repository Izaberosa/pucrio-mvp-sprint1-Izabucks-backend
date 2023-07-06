from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union

from  model import Base


class Bebida(Base):
    __tablename__ = 'bebida'

    id = Column("pk_bebida", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    descricao = Column(String(4000))
    imagem_path = Column(String(2048))
    valor = Column(Float)
    categoria = Column(String(200))
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, nome:str, descricao:str,imagem_path:str,
                      valor:float, categoria: str,
                      data_insercao:Union[DateTime, None] = None):
        """
        Cria uma nova Bebida no Cardapio 

        Arguments:
            nome: Nome Da Bebida.
            descricao: Descrição da Bebida.
            imagem_path: Caminho ou URL de acesso a imagem da bebida
            valor: valor da bebida 
            categoria: identifica a categoria da bebida
            data_insercao: data de quando foi inserido à bebida
        """
        self.nome = nome
        self.descricao = descricao
        self.imagem_path = imagem_path
        self.valor = valor
        self.categoria = categoria
        if data_insercao:
            self.data_insercao = data_insercao
