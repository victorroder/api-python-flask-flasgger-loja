from flask import Blueprint, request, jsonify
categorias_bp = Blueprint('categorias', __name__)
data = []

@categorias_bp.route('/', methods=['GET'])
def get(): return jsonify(data)

@categorias_bp.route('/', methods=['POST'])
def post():
    obj = request.json
    obj["id"] = len(data)+1
    data.append(obj)
    return jsonify(obj)

@categorias_bp.route('/<int:id>', methods=['PUT'])
def put(id):
    for i in data:
        if i["id"]==id:
            i.update(request.json)
            return jsonify(i)
    return {"erro":"não encontrado"},404

@categorias_bp.route('/<int:id>', methods=['DELETE'])
def delete(id):
    global data
    data = [i for i in data if i["id"]!=id]
    return {"msg":"ok"}
