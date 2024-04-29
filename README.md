# FASTAPI-Loja

# API de Gerenciamento de Produtos

Esta é uma API simples para gerenciamento de produtos, construída com FastAPI em Python.

Funcionalidades
- Listar todos os produtos
- Obter detalhes de um produto específico por ID
- Criar um novo produto
- Atualizar os detalhes de um produto existente
- Deletar um produto existente

Endpoints
- Listar Produtos
GET /produtos/Retorna uma lista de todos os produtos disponíveis.
- Obter Produto por ID
GET /produtos/{produto_id}Retorna os detalhes de um produto específico com base no ID fornecido.
- Criar Produto
POST /produtos/Cria um novo produto com os detalhes fornecidos no corpo da solicitação.
- Atualizar Produto
PUT /produtos/{produto_id}Atualiza os detalhes de um produto existente com base no ID fornecido.
- Deletar Produto
DELETE /produtos/{produto_id}Deleta um produto existente com base no ID fornecido.

Modelo de Dados

A API espera e retorna dados no formato JSON seguindo o modelo de dados: {
  "id": "int",
  "nome": "str",
  "preco": "float"
}

# Certifique-se de ter todas as dependências instaladas. Você pode instalá-las executando:
- pip install fastapi uvicorn

# Para iniciar o servidor, execute o seguinte comando:
- uvicorn main:app --reload
- O servidor será iniciado em http://127.0.0.1:8000.
