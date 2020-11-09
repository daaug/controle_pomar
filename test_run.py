from requests import get, post, put, delete

localhost = "http://localhost:5000"

dados_especie = [
    {"especie": "Fuji", "descricao": "A Maçã Fuji é um clone de maçã desenvolvida por cultivadores da Estação de Pesquisa de Tohoku em Fujisaki", "arvore_codigo": "MAC"},
    {"especie": "Maca-verde", "descricao": "A maçã-verde, conhecida também pelo nome varietal de Granny Smith, é uma variedade de maçã. Trata-se de uma maçã normal", "arvore_codigo": "MAC"},
    {"especie": "McIntosh", "descricao": "A Red McIntosh ou somente McIntosh é um tipo de maçã originalmente cultivada no leste do Canadá e na Nova Inglaterra", "arvore_codigo": "MAC"},
    {"especie": "Pera-laranja", "descricao": "É fácil identificar a laranja-pêra entre muitas, já que ela é menor que as demais e possui um formato um pouquinho mais alongado", "arvore_codigo": "LAR"},
    {"especie": "Bahia-laranja", "descricao": "Popularmente conhecida como laranja-de-umbigo por possuir uma pequena saliência em sua casca, que é super alaranjada", "arvore_codigo": "LAR"},
    {"especie": "Lima-laranja", "descricao": "A laranja-lima é a mais indicada para o começo da alimentação com frutas de bebês por não ter nenhuma acidez", "arvore_codigo": "LAR"}
]

dados_arvore = [
    {"arvore": "Macieira", "descricao": "Acredita-se que as macieiras são cultivadas desde o século III A.C., especialmente na Ásia.", "idade": 35, "grupo_codigo": "MACA"},
    {"arvore": "Laranjeira", "descricao": "É uma árvore de pequeno porte, em torno de 8,0 metros de altura, tronco de casca acinzentada, muito ramificada de copa densa com forma arredondada.", "idade": 58, "grupo_codigo": "LARA"}
]

dados_grupo = [
    { "nome": "laranjas", "descricao": "Grupo destinado a laranjas e laranjos"},
    { "nome": "macas", "descricao": "Grupo destinado a macas"}
]

dados_colheita = [
    {"info": "Colheita efetuada usando capivaras", "data_colheita": "12/08/2016", "peso_bruto": 14.8, "especie_codigo": "PER"},
    {"info": "Colheita efetuada usando maquinas", "data_colheita": "07/06/2015", "peso_bruto": 10.2, "especie_codigo": "FUJ"},
    {"info": "Colheita efetuada pela minha avó", "data_colheita": "02/01/2019", "peso_bruto": 20.9, "especie_codigo": "MCI"},
    {"info": "Eu colhi isso", "data_colheita": "29/04/2020", "peso_bruto": 2.2, "especie_codigo": "BAH"}
]

post(localhost + "/grupo", json=dados_grupo).json()
post(localhost + "/arvore", json=dados_arvore).json()
post(localhost + "/especie", json=dados_especie).json()
post(localhost + "/colheita", json=dados_colheita).json()