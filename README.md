# Teste Técnico - Indico

Teste técnico desenvolvido para Indico, construído utilizando Flask, Flask-SQLAlchemy e SQLite3, com padronização de erros.

## Índice

1. Descrição
2. Tecnologias Utilizadas
3. Instalação
4. Como Usar
5. Padronização de Erros

## Descrição

Este projeto consiste em uma aplicação web desenvolvida com Flask e Flask-SQLAlchemy, utilizando SQLite3 como banco de dados. O objetivo é construir uma aplicação que cadastra lojas de Fast Food, podendo ser feitas com a utilização de arquivos CSV.

## Tecnologias Utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLite3

## Instalação

1. Clone o repositório:
   ```sh
   git clone https://github.com/MatheusSantos2003/indico-fast-food-stores.git
   ```
2. Navegue até o diretório do projeto:
   ```sh
   cd indico-fast-food-stores
   ```
3. Crie um ambiente virtual:
   ```sh
   python3 -m venv venv
   # ou qualquer outro ambiente de sua preferencia
   ```
4. Ative o ambiente virtual:
   - No Windows:
     ```sh
     venv\Scripts\activate
     ```
   - No MacOS/Linux:
     ```sh
     source venv/bin/activate
     ```
5. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

## Como Usar

1. Inicie a base de dados da aplicação Flask:
   ```sh
   flask db init
   flask db upgrade
   flask db migrate
   ```
2. Inicie a aplicação:
   ```sh
   flask run
   ```
2. Acesse a aplicação no seu navegador:
   ```sh
   http://127.0.0.1:5000/stores
   ```
   Inicialmente nesta página é possivel realizar a importação das lojas pelo arquivo csv fornecido no inicio do teste técnico.

## Rotas da Aplicação

### Listar todas as lojas

- **Rota:** `/stores/list`
- **Método:** GET
- **Descrição:** Retorna uma lista de todas as lojas.

### Buscar uma loja por ID

- **Rota:** `/stores/find/<id>`
- **Método:** GET
- **Descrição:** Retorna uma loja específica pelo seu ID.

### Deletar uma loja por ID

- **Rota:** `/stores/delete/<id>`
- **Método:** DELETE
- **Descrição:** Deleta uma loja específica pelo seu ID.

### Atualizar uma loja por ID

- **Rota:** `/stores/update/<id>`
- **Método:** PUT
- **Descrição:** Atualiza uma loja específica pelo seu ID com os dados fornecidos no corpo da requisição.

### Criar uma nova loja

- **Rota:** `/stores/create`
- **Método:** POST
- **Descrição:** Cria uma nova loja com os dados fornecidos no corpo da requisição.

### Importar CSV - Renderização do Template

- **Rota:** `/stores/`
- **Método:** GET
- **Descrição:** Renderiza o template para importar um arquivo CSV.

### Importar CSV - Processamento do Arquivo

- **Rota:** `/stores/import-csv`
- **Método:** POST
- **Descrição:** Recebe um arquivo CSV vindo do enpoint `/stores/`  e importa os dados para o banco de dados.
    
   

## Padronização de Erros

Todos os erros da aplicação foram padronizados, utilizando extensions do Flask, criados no arquivo `exception_extensions.py`

Exemplo de resposta de erro:

```json
  {
  	"code": 404,
  	"error": "NotFound",
  	"message": "Store not found"
  }
```

