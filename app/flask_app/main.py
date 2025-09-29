from flask import Flask, Blueprint, url_for, redirect
from flask_app.rotas.pergunta_simples import pergunta_simples
from flask_app.rotas.resposta_estruturada import resposta_estruturada
from flask_app.rotas.rag import rag

web_framework = Flask(__name__)
route_root = Blueprint('route_root', __name__)

web_framework.register_blueprint(route_root)
web_framework.register_blueprint(pergunta_simples)
web_framework.register_blueprint(resposta_estruturada)
web_framework.register_blueprint(rag)

@web_framework.route("/", endpoint="index", methods=['GET'])
def index():
    return redirect(url_for("pergunta_simples.perguntar"))
    
