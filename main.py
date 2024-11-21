from fastapi import FastAPI
from pydantic import BaseModel, Field

aplicativo = FastAPI()

# Teste2

# Classe para todas as listas
class Lista(BaseModel):
    lista: list[int]

@app.get("/")
async def root():
    return {"mensagem": "Hello World"}

lista_b1 = []

@app.post("/adicionar-elementos-lista", response_model=Lista)
async def root(payload: Lista):
    lista_aux = []
    for item in payload.lista:
        lista_aux.append(item)
        lista_b1.append(item)

    response = {
        "lista": lista_b1
        }
    return response

@app.post("/listar-pares", response_model=Lista)
async def listar_pares(payload: Lista):
    """
        ### Função listar pares

        recebe uma lista de inteiros e retorna uma lista de valores pares

        ```
            input -> lista_inteiros = [1,2,3,4]
            output -> lista_pares = [2,4]
        ```
    """
    nova_lista = []
    for item in payload.lista:
        if item % 2 == 0:
            nova_lista.append(item)
    response = {
        "lista_pares": nova_lista
        }
    return response

@app.get("/listar-pares-banco", response_model=Lista)
async def listar_pares():
    nova_lista = []
    for item in lista_b1:
        if item % 2 == 0:
            nova_lista.append(item)
    response = {
        "lista_pares": nova_lista
        }
    return response