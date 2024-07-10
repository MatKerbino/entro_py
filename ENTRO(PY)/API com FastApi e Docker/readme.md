# WorkoutAPI

WorkoutAPI é uma aplicação API moderna e de alta performance desenvolvida com FastAPI. É uma API voltada para competições de CrossFit, unindo duas paixões: programação e treino. Esta API é projetada para ser prática e educativa, com foco em conceitos fundamentais e utilização de ferramentas poderosas.

## Framework e Ferramentas Utilizadas

- **FastAPI**: Framework web moderno e rápido, ideal para a construção de APIs com suporte para Python 3.6 ou superior. Utiliza type hints padrão do Python para fornecer alta performance e facilidade de codificação.
- **Async**: O código assíncrono permite que o programa execute outras tarefas enquanto aguarda a finalização de operações demoradas, melhorando a eficiência.
- **SQLAlchemy**: ORM (Object-Relational Mapping) que facilita a interação com bancos de dados.
- **Alembic**: Ferramenta de migração de banco de dados para SQLAlchemy.
- **Pydantic**: Biblioteca para validação de dados e definição de modelos de dados com suporte a type hints.
- **PostgreSQL**: Banco de dados relacional utilizado para armazenar os dados, executado por meio do Docker.
- **Docker**: Utilizado para containerização e fácil gerenciamento do banco de dados.
- **FastAPI Pagination**: Biblioteca para adicionar paginação aos endpoints da API.

## Modelagem de Entidade e Relacionamento (MER)

A API foi modelada com um MER simplificado, adequado para o objetivo educacional e hands-on do projeto. As tabelas e relações foram projetadas para cobrir os requisitos básicos de uma aplicação de competição de CrossFit.

## Execução e Desenvolvimento

Para o desenvolvimento, utilizamos `pyenv` para gerenciar o ambiente virtual com a versão 3.11.4 do Python. A instalação das dependências é gerenciada pelo `pip`, utilizando um arquivo `requirements.txt`.

## Endpoints e Funcionalidades

### Query Parameters

- **Atleta**:
  - `nome`: Filtra atletas pelo nome.
  - `cpf`: Filtra atletas pelo CPF.

### Customização de Responses

- **Get All**:
  - **Atleta**:
    - `nome`
    - `centro_treinamento`
    - `categoria`

### Manipulação de Exceções

- Trata a exceção `sqlalchemy.exc.IntegrityError` e retorna a mensagem: “Já existe um atleta cadastrado com o cpf: x”, com status code 303.

### Paginação

- Implementação de paginação nos endpoints utilizando a biblioteca `fastapi-pagination` com suporte para `limit` e `offset`.
