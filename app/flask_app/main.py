from flask import Flask, Blueprint, render_template, url_for, redirect, request
from flask_app.template_models.Rag import Rag
from suporte.Rag import Rag as RagDomain
from flask_app.rotas.pergunta_simples import pergunta_simples
from flask_app.rotas.resposta_estruturada import resposta_estruturada
from suporte.ContarDesempenhoPergunta import ContarDesempenhoPergunta

web_framework = Flask(__name__)
route_root = Blueprint('route_root', __name__)
web_framework.register_blueprint(route_root)
web_framework.register_blueprint(pergunta_simples)
web_framework.register_blueprint(resposta_estruturada)

@web_framework.route("/", endpoint="index", methods=['GET'])
def index():
    return redirect(url_for("perguntar"))
    
@web_framework.route('/rag', endpoint="rag", methods=['GET'])
def rag():
    return render_template("rag.html", view_model=Rag())

@web_framework.route('/rag_enviar', endpoint="rag_enviar", methods=['POST'])
def rag_enviar():
    pergunta = request.get_json().get('pergunta')
    
    rag = RagDomain()
    contar_desempenho_pergunta = ContarDesempenhoPergunta(rag)
    contar_desempenho_pergunta.pergunta = pergunta
    contar_desempenho_pergunta.executar()
    
    return {
        "resposta": contar_desempenho_pergunta.buscar_resposta()
    }
