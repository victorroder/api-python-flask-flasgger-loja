from flask import Flask
from flasgger import Swagger
from routes.clientes import clientes_bp
from routes.produtos import produtos_bp
from routes.pedidos import pedidos_bp
from routes.categorias import categorias_bp

app = Flask(__name__)
Swagger(app)

app.register_blueprint(clientes_bp, url_prefix="/clientes")
app.register_blueprint(produtos_bp, url_prefix="/produtos")
app.register_blueprint(pedidos_bp, url_prefix="/pedidos")
app.register_blueprint(categorias_bp, url_prefix="/categorias")

if __name__ == "__main__":
    app.run(debug=True)
