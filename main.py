from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Lista(BaseModel):
    lista: list[int]

class ListaPares(BaseModel):
    lista_pares: list[int]

@app.get("/")
async def root():
    return {"message": "Hello World"}

lista = []

@app.post("/adicionar-elementos-lista", response_model=Lista)
async def root(payload: Lista):
    lista_aux = []
    for item in payload.lista:
        lista_aux.append(item)
        lista.append(item)

    return {"lista": lista}

@app.post("/listar-pares", response_model=ListaPares)
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
    return {"lista_pares": nova_lista}

@app.get("/listar-pares-banco", response_model=ListaPares)
async def listar_pares():
    nova_lista = []
    for item in lista:
        if item % 2 == 0:
            nova_lista.append(item)
    return {"lista_pares": nova_lista}