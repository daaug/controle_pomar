from app import db


class Especie(db.Model):
    __tablename__ = 'especies'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String)
    especie = db.Column(db.String)
    descricao = db.Column(db.Text)

    arvore_codigo = db.Column(db.String, db.ForeignKey('arvores.codigo'))
    arvore = db.relationship('Arvore', foreign_keys=arvore_codigo)


class Arvore(db.Model):
    __tablename__ = 'arvores'

    id = db.Column(db.Integer, primary_key=True)
    codigo = db.Column(db.String)
    arvore = db.Column(db.String)
    descricao = db.Column(db.Text)
    idade = db.Column(db.Integer)

    grupo_codigo = db.Column(db.String, db.ForeignKey('grupos.codigo'))
    grupo = db.relationship('Grupo', foreign_keys=grupo_codigo)


class Grupo(db.Model):
    __tablename__ = 'grupos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String, unique=True)
    descricao = db.Column(db.Text)
    codigo = db.Column(db.String)


class Colheita(db.Model):
    __tablename__ = 'colheitas'

    id = db.Column(db.Integer, primary_key=True)
    info = db.Column(db.Text)
    data_colheita = db.Column(db.String)
    peso_bruto = db.Column(db.Float)

    especie_codigo = db.Column(db.String, db.ForeignKey('especies.codigo'))
    especie = db.relationship('Especie', foreign_keys=especie_codigo)
