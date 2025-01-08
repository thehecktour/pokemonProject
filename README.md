# Projeto Pokémon FastAPI


##### Este projeto é uma API simples construída com FastAPI que interage com a PokeAPI para buscar informações sobre Pokémon, especificamente suas habilidades. A aplicação permite que o usuário insira o nome de um Pokémon e receba uma lista de suas habilidades.


### Visão Geral

A aplicação permite ao usuário:

Enviar o nome de um Pokémon através de um formulário HTML.
Obter as habilidades associadas ao Pokémon, que são então apresentadas na interface do usuário.
Utiliza FastAPI para o backend e Jinja2 para renderizar os templates HTML.


### Tecnologias Usadas


FastAPI: Framework para construção de APIs rápidas e eficientes.
Jinja2: Motor de templates para renderização de HTML.
httpx: Cliente HTTP assíncrono utilizado para consumir a PokeAPI.
Poetry: Gerenciador de dependências para o projeto Python.
Uvicorn: Servidor ASGI para rodar a aplicação FastAPI.

### Instalação


Python 3.12+
Poetry
Docker (opcional)

### Passos para Instalação


1. Instale o Python 3.12+ em seu sistema.
2. Instale o Poetry: `pip install poetry`
3. Clone o repositório: `git clone https://github.com/your_username/pokemon_fastapi.git`
4. Entre na pasta do projeto: `cd pokemon_fastapi`
5. Rode o comando: `poetry install`
6. Rode o comando: `poetry run uvicorn main:app --reload`

Você poderá rodar TAMBÉM executando o Docker, caso você saiba trabalhar com ele.

### Exemplo de Uso

1. Acesse http://localhost:8000/ no navegador.
2. No formulário, insira o nome de um Pokémon, como "Pikachu", e clique em "Buscar".
3. As habilidades do Pokémon serão exibidas na tela.


### Dockerização

O projeto pode ser containerizado usando Docker para facilitar o deployment ou execução local.

Passos para Dockerizar


1. Construir a imagem Docker:

bash
````
docker build -t pokemon-fastapi .

````


2. Rodar o contêiner:

bash
`````
docker run -d -p 8000:8000 pokemon-fastapi

`````

3. A aplicação estará acessível em http://localhost:8000.


### Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais informações.

