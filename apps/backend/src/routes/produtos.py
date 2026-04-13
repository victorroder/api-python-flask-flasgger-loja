from flask import Blueprint, request, jsonify
produtos_bp = Blueprint('produtos', __name__)
data = []

@produtos_bp.route('/', methods=['GET'])
def get(): return jsonify(data)

@produtos_bp.route('/', methods=['POST'])
def post():
    obj = request.json
    obj["id"] = len(data)+1
    data.append(obj)
    return jsonify(obj)

@produtos_bp.route('/<int:id>', methods=['PUT'])
def put(id):
    for i in data:
        if i["id"]==id:
            i.update(request.json)
            return jsonify(i)
    return {"erro":"não encontrado"},404

@produtos_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    global data
    data = [i for i in data if i["id"]!=id]
    return {"msg":"ok"}
