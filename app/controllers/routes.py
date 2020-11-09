from app import app, db, jsonify, request
from app.models.classes import Especie, Arvore, Grupo, Colheita
from flask import render_template


@app.route('/', methods=['GET'])
def home():
    colheita = db.session.query(Especie, Arvore, Grupo, Colheita).select_from(Arvore).join(Especie).join(Grupo).join(Colheita).all()
    return render_template('index.html', colheita=colheita)


@app.route('/especie', methods=['POST'])
def createEspecie():
    req = request.json if type(request.json) == 'list' else list(request.json)

    for r in req:
        especie = Especie(especie=r['especie'], descricao=r['descricao'], codigo=r['especie'][:3].upper(), arvore_codigo=r['arvore_codigo'])
        db.session.add(especie)

    db.session.commit()

    return "Especie created!", 201


@app.route('/arvore', methods=['POST'])
def createArvore():
    req = request.json if type(request.json) == 'list' else list(request.json)

    for r in req:
        arvore = Arvore(arvore=r['arvore'], idade=r['idade'], descricao=r['descricao'], grupo_codigo=r['grupo_codigo'], codigo=r['arvore'][:3].upper())
        db.session.add(arvore)

    db.session.commit()

    return "Arvore created!", 201


@app.route('/grupo', methods=['POST'])
def createGrupo():
    req = request.json if type(request.json) == 'list' else list(request.json)

    for r in req:
        grupo = Grupo(nome=r['nome'], descricao=r['descricao'], codigo=r['nome'][:4].upper())
        db.session.add(grupo)

    db.session.commit()

    return "Group created!", 201


@app.route('/colheita', methods=['POST'])
def createColheita():
    req = request.json if type(request.json) == 'list' else list(request.json)

    for r in req:
        colheita = Colheita(info=r['info'], data_colheita=r['data_colheita'], peso_bruto=r['peso_bruto'], especie_codigo=r['especie_codigo'].upper())
        db.session.add(colheita)

    db.session.commit()

    return "Colheita created!", 201
