from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Produto(BaseModel):
    id: int
    nome: str
    preco: float

# Dados em memória
produtos = [
    {
        "id": 1,
        "nome": "Camiseta",
        "preco": 29.99
    },
    {
        "id": 2,
        "nome": "Calça Jeans",
        "preco": 79.90
    }
]

@app.get("/")
def pagina_inicial():
    return {"message": "Acesse /produtos para ver os produtos."}

@app.get("/produtos/", response_model=list[Produto])
def listar_produtos():
    return produtos

@app.get("/produtos/{produto_id}", response_model=Produto)
def obter_produto(produto_id: int):
    for prod in produtos:
        if prod.get("id") == produto_id:
            return prod
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.post("/produtos/", response_model=Produto, status_code=201)
def criar_produto(produto: Produto):
    produtos.append(produto)
    return produto

@app.put("/produtos/{produto_id}", response_model=Produto)
def atualizar_produto(produto_id: int, produto: Produto):
    for index, prod in enumerate(produtos):
        if prod.get("id") == produto_id:
            produtos[index]["nome"] = produto.nome
            produtos[index]["preco"] = produto.preco
            return produto
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete("/produtos/{produto_id}", response_model=dict)
def deletar_produto(produto_id: int):
    for index, prod in enumerate(produtos):
        if prod.get("id") == produto_id:
            del produtos[index]
            return {"message": "Produto deletado"}
    raise HTTPException(status_code=404, detail="Produto não encontrado")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
