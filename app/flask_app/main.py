from flask import Flask, Blueprint, render_template, url_for, redirect
from flask_app.template_models.Rag import Rag
from flask_app.rotas.pergunta_simples import pergunta_simples
from flask_app.rotas.resposta_estruturada import resposta_estruturada

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
