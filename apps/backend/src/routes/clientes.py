from flask import Blueprint, request, jsonify
clientes_bp = Blueprint('clientes', __name__)
data = []

@clientes_bp.route('/', methods=['GET'])
def get(): return jsonify(data)

@clientes_bp.route('/', methods=['POST'])
def post():
    obj = request.json
    obj["id"] = len(data)+1
    data.append(obj)
    return jsonify(obj)

@clientes_bp.route('/<int:id>', methods=['PUT'])
def put(id):
    for i in data:
        if i["id"]==id:
            i.update(request.json)
            return jsonify(i)
    return {"erro":"não encontrado"},404

@clientes_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    global data
    data = [i for i in data if i["id"]!=id]
    return {"msg":"ok"}
