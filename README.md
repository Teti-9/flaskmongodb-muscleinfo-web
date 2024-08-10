## Flask + MongoDB

Esse é um projeto back-end para procurar informações sobre exercícios físicos. Permite adicionar, procurar, editar ou deletar informações sobre exercícios dentro de uma database mongoDB. A API é feita usando Flask e segue um modelo RESTful.

### Instalação
```
git clone https://github.com/Teti-9/flaskmongodb-muscleinfo-web.git
cd flaskmongodb-muscleinfo-web
```
```
pip install -r requirements.txt
```
```
Garanta que você tenha MongoDB instalado.
Crie uma database e uma collection requiridos para aplicação funcionar.
Crie um arquivo .env com a url da database ou edite o arquivo database.py diretamente.
```
```
Rode a aplicação na pasta raíz do projeto:
python main.py
```

### Endpoints
```
- Popular database
    - Endpoint: /popular
    - Method: POST
    - Request Body: Json
{
    "nome": "Nome do exercício.",
    "musculo": "Músculo principal.",
    "info": "Informações sobre o exercício.",
    "dicas": "Dicas no geral, exemplo: execução."
}
```
```
- Procurar por grupo muscular
    - Endpoint: /<musculo>
    - Method: GET
```
```
- Editar info exercício
    - Endpoint: /editar
    - Method: PUT
    - Request Body: Json
{
    "nome": "Nome do exercício.",
    "info": "Informações extras ou atualizadas sobre o exercício.",
}
```
```
- Deletar exercício
    - Endpoint: /deletar
    - Method: DELETE
    - Request Body: Json
{
    "nome": "Nome do exercício."
}
```