from flask import Blueprint, request, jsonify
from src.infra.mongodb.repositorios.repositorio import RepositorioExercicios
from src.infra.mongodb.models.models import Exercicios
from pydantic import ValidationError

routers = Blueprint("routers", __name__)

@routers.route("/popular", methods=["POST"])
def popular_db():
    try:
        data = request.get_json()
    except:
        return jsonify({"Erro de validação": "Nenhum campo detectado!"}), 400
    nome, musculo, info, dicas = data.get('nome'), data.get('musculo'), data.get('info'), data.get('dicas')
    try:
        template = Exercicios(nome=nome, 
                            musculo=musculo, 
                            info=info, 
                            dicas=dicas)
    except ValidationError:
        return jsonify({"Erro de validação": "Campos incorretos!"}), 400
    RepositorioExercicios.criar_estrutura(template)
    return jsonify({"Sucesso": "Template criado com sucesso!"}), 201

@routers.route("/<musculo>", methods=["GET"])
def procurar_musculo_rota(musculo):
    musculo = musculo.split(',')
    lista = []
    erros = []
    
    page = int(request.args.get('page', 1))
    limit = int(request.args.get('limit', 5))
    skip = (page - 1) * limit

    for i in musculo:
        exercicios = RepositorioExercicios.procurar_musculo(i)
        if not exercicios:
            erros.append(f"Não existe um grupamento muscular chamado '{i}'.")
        else:
            lista.extend(exercicios)

    paginated_lista = lista[skip:skip + limit]

    response = {
        "Página atual": page,
        "Limite de exercícios por página": limit,
        "Total de exercícios pesquisados": len(lista),
        "Total de páginas": (len(lista) + limit - 1) // limit,
        "Exercícios encontrados": paginated_lista
    }

    if erros:
        response["Erros"] = erros

    return jsonify(response), 200

@routers.route('/editar', methods=["PUT"])
def editar_musculo():
    try:
        data = request.get_json()
    except:
        return jsonify({"Erro de validação": "Nenhum campo detectado!"}), 400
    
    nome, info = data.get('nome'), data.get('info')
    
    search = RepositorioExercicios.procurar_exercicio(nome)
    if search:
        RepositorioExercicios.editar_musculo(nome, info)
        return jsonify(f'Informações sobre o músculo {nome} editadas com sucesso!'), 200
    else:
        return jsonify(f'Músculo {nome} não existe na database!'), 400

@routers.route('/deletar', methods=['DELETE'])
def deletar_musculo():
    try:
        data = request.get_json()
    except:
        return jsonify({"Erro de validação": "Nenhum campo detectado!"}), 400
    
    nome = data.get('nome')

    search = RepositorioExercicios.procurar_exercicio(nome)
    if search:
        RepositorioExercicios.deletar_musculo(nome)
        return jsonify(f'Músculo {nome} deletado com sucesso!'), 200
    else:
        return jsonify(f'Músculo {nome} não existe na database!'), 400