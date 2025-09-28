from flask import Flask, Blueprint, render_template, url_for, redirect, request
from flask_app.template_models.Rag import Rag
from suporte.Rag import Rag as RagDomain
from flask_app.rotas.pergunta_simples import pergunta_simples
from flask_app.rotas.resposta_estruturada import resposta_estruturada
from suporte.ContarDesempenhoPergunta import ContarDesempenhoPergunta
from suporte.Banco import Banco
from suporte.Utilidades import Utilidades

web_framework = Flask(__name__)
route_root = Blueprint('route_root', __name__)

web_framework.register_blueprint(route_root)
web_framework.register_blueprint(pergunta_simples)
web_framework.register_blueprint(resposta_estruturada)

@web_framework.route("/", endpoint="index", methods=['GET'])
def index():
    return redirect(url_for("pergunta_simples.perguntar"))
    
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
    
    # raise Exception("Parado 17")
    
    banco = Banco()
    banco.registrar_pergunta(pergunta)
    id_pergunta = banco.ultimo_id_inserido
    dados_desempenho = contar_desempenho_pergunta.dados_desempenho
    
    banco.registrar_resposta(
        resposta=contar_desempenho_pergunta.resposta,
        id_pergunta=id_pergunta,
        timestamp_antes=dados_desempenho["timestamp_antes"],
        timestamp_depois=dados_desempenho["timestamp_depois"],
        diferenca_ms=dados_desempenho["diferenca_ms"]
    )
    
    return {
        "resposta": contar_desempenho_pergunta.resposta
    }
