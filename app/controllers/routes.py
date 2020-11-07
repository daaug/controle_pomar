from app import app, jsonify, request


devs = [
    {
        'nome': 'augusto',
        'lang': 'c++'
    }
]

@app.route('/', methods=['GET'])
def home():
    return {'msg': 'Running good'}


@app.route('/show', methods=['GET'])
def show():
    return jsonify(devs), 200


@app.route('/create', methods=['POST'])
def create():
    devs.append(request.json)
    return request.json
