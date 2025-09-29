from flask import Flask, Blueprint, url_for, redirect
from flask_app.rotas.pergunta_simples import pergunta_simples
from flask_app.rotas.resposta_estruturada import resposta_estruturada
from flask_app.rotas.rag import rag
from suporte.Banco import Banco

web_framework = Flask(__name__)
route_root = Blueprint('route_root', __name__)

web_framework.register_blueprint(route_root)
web_framework.register_blueprint(pergunta_simples)
web_framework.register_blueprint(resposta_estruturada)
web_framework.register_blueprint(rag)

def arquivo_e_ativo(arquivo: str) -> bool:
    banco = Banco()
    return banco.arquivo_esta_ativo(arquivo)

@web_framework.context_processor
def inject_functions():
    return {
        'arquivo_e_ativo': arquivo_e_ativo
    }

@web_framework.route("/", endpoint="index", methods=['GET'])
def index():
    return redirect(url_for("pergunta_simples.perguntar"))
    
