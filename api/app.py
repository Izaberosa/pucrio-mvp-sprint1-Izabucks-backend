from email.mime import base
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote

from flask_openapi3 import Info, Tag
from flask_openapi3 import OpenAPI
from flask_cors import CORS
from flask import redirect
from model import Session, Bebida
from logger import logger
from schemas import *


info = Info(title="Izabucks", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# definindo tags
bebida_tag = Tag(name="Cardapio de bebida", description=" Com essa Api você consegue Adicionar Visualizar e remover nossas bebidas do cardapio")


@app.get('/')
def home():
    return redirect('/openapi')


@app.post('/bebida/adicionar', tags=[bebida_tag],
          responses={"200": BebidaViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def add_bebida(form: BebidaSchema):
    """Adiciona uma nova Bebida a Cardapio à base de dados

    Retorna uma dos produtos e comentários associados.
    """
    session = Session()
    bebida = Bebida(
        nome=form.nome,
        descricao=form.descricao,
        valor=form.valor,
        imagem_path=form.imagem,
        categoria=form.categoria
        )
    logger.debug(f"Adicionando uma bebida de nome: '{bebida.nome}'")
    try:
        session = Session()
        # adicionando uma nova bebida
        session.add(bebida)
        # efetivando o camando de adicionar uma nova bebida  na tabela
        session.commit()
        logger.debug(f"Adicionado bebida de nome: '{bebida.nome}'")
        return apresenta_bebida(bebida), 200
    except IntegrityError as e:
        error_msg = "Bebida de mesmo nome já salvo na base :/"
        logger.warning(f"Erro ao adicionar bebida '{bebida.nome}', {error_msg}")
        return {"mesage": error_msg}, 409
    except Exception as e:
        error_msg = "Não foi possível salvar uma nova bebida no cardapio :/"
        logger.warning(f"Erro ao adicionar uma nova bebida '{bebida.nome}', {error_msg}")
        return {"mesage": error_msg}, 400


@app.get('/bebida/lista', tags=[bebida_tag],
         responses={"200": BebidaViewSchema, "404": ErrorSchema})
def get_bebida(query: BebidaBuscaSchema):
    """Faz a busca por um Produto a partir do id do produto

    Retorna uma representação dos produtos e comentários associados.
    """
    bebida_id = query.id
    logger.debug(f"Coletando dados sobre bebida #{bebida_id}")
    session = Session()
    bebida = session.query(Bebida).filter(Bebida.id == bebida_id).first()
    if not bebida:
        error_msg = "Bebida não encontrado na base :/"
        logger.warning(f"Erro ao buscar produto '{bebida_id}', {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Produto econtrado: '{bebida.nome}'")
        return apresenta_bebida(bebida), 200


@app.get('/bebida/listas', tags=[bebida_tag],
         responses={"200": BebidaListaViewSchema, "404": ErrorSchema})
def get_bebidas():
    """Lista todos as bebidas cadastradas na nossa base

    Retorna uma lista de representações das nossas bebidas do cardapio.
    """
    logger.debug(f"Coletando lista de bebidas do cardapio")
    session = Session()
    bebida = session.query(Bebida).all()
    print(bebida)
    if not bebida:
        error_msg = "Bebida não encontrado na base :/"
        logger.warning(f"Erro ao buscar por lista de bebida do nosso cardapio. {error_msg}")
        return {"mesage": error_msg}, 400
    else:
        logger.debug(f"Retornando lista de bebidas")
        return apresenta_bebidas(bebida), 200


@app.delete('/bebida/deletar', tags=[bebida_tag],
            responses={"200": BebidaDelSchema, "404": ErrorSchema})
def del_bebida(query: BebidaBuscaSchema):
    """Deleta uma bebida a partir do id informado

    Retorna uma mensagem de confirmação da remoção.
    """
    bebida_nome = unquote(unquote(query.nome))
    print(bebida_nome)
    logger.debug(f"Deletando dados sobre as  bebidas #{bebida_nome}")
    # criando conexão com a base
    session = Session()
    # fazendo a remoção
    count = session.query(Bebida).filter(Bebida.nome == bebida_nome).delete()
    session.commit()

    if count:
        # retorna a representação da mensagem de confirmação
        logger.debug(f"Deletado bebidas #{bebida_nome}")
        return {"mesage": "Bebida removida", "id": bebida_nome}
    else:
        # se o produto não foi encontrado 
        error_msg = "Bebida não encontrada na base :/"
        logger.warning(f"Erro ao deletar bebida #'{bebida_nome}', {error_msg}")
        return {"mesage": error_msg}, 404

