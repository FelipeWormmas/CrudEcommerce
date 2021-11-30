from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Categoria(BaseModel):
    name: str
    description: str


class Comprador(BaseModel):
    cpf: str
    name: str
    address: str
    value: int

class CompradorPUT(BaseModel):
    cpf: str
    name: str
    address: str
    value: int

class Fornecedor(BaseModel):
    product: str
    address: str
    cnpj: str

class Produto(BaseModel):
    name: str
    value: int
    qtd: int


categoria = []
comprador = []
fornecedor = []
produto = []


@app.post('/comprador', status_code=status.HTTP_201_CREATED)
def adicionar_comprador(comprador: Comprador):
    comprador.append(comprador)


@app.get('/comprador')
def lista_comprador():
    return comprador


@app.delete('/comprador/{cpf}', status_code=status.HTTP_204_NO_CONTENT)
def remover_comprador(cpf: str):
    resultado = list(filter(lambda a: a[1].cpf == cpf, enumerate(comprador)))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Aluno com o cpf: {cpf} nao foi encontrado')

    i, _ = resultado[0]
    del comprador[i]


@app.put('/comprador/{cpf}')
def atualizar_comprador(cpf: str, comprador_atualizado: CompradorPUT):
    resultado = list(filter(lambda a: a.cpf == cpf, comprador))
    if not resultado:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'comprador com o cpf: {cpf} não foi encontrado')

    comprador.name = comprador_atualizado.name
    comprador.address = comprador_atualizado.address
    comprador.value = comprador_atualizado.value
    comprador.cpf = comprador_atualizado.cpf

    return comprador

