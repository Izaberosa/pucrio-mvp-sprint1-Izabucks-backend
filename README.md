# API IzaBucks 

Este é um projeto que faz parte da entrega do MVP 

Izabucks : Api tem como função disponibiliza a consulta, criação , edição e exclusão de bebidas do cardapio. Single page application (SPA) consumindo o dado de uma API em vez do acesso aos dados estáticos de um arquivo JSON.

---
## Como instalar e executar a API


Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

> É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

```
(env)$ pip install -r requirements.txt
```

Requisitos:

Realizar a instalação das libs python listadas no requirements.txt.
É recomendado o uso de ambientes virtuais do tipo virtualenv.
1 - Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo:

cd pucrio-mvp-sprint1-Izabucks-backend.git

2 - Instalar Virtualenv

$ pip install VirtualEnv
3 - Criar Virtualenv

$ Virtualenv venv
4 - Ativar venv

$ .\env\Scripts\activate
5 - Instalar libs python, rodar o comando no terminal powershell

(venv)$ pip install -r requirements.txt
6 - Instalar Greenlet

(venv)$ pip install greenlet
7 - Executar API:

(venv)$ flask run --host 0.0.0.0 --port 5000
Em caso de modificações no código enquanto a API estiver rodando, utilizar o parâmetro reload, que reiniciará o servidor automaticamente após uma mudança no código fonte.

(env)$ flask run --host 0.0.0.0 --port 5000 --reload
Após seguir todos os passos, abrir o link abaixo no bavegador para verificar o status da API em execução

http://localhost:5000/#/
Link para Documentação:

[http://127.0.0.1:5000/openapi/]

#Executar Docker 
1.docker build -t rest-d . (cria a imagem no docker )
2.docker run -p 5000:5000 rest-d (executar container criado na imagem)
3.docker rmi rest-d excluir imagem (excluir imagem rest-d) 
