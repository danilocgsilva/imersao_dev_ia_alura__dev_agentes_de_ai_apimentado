from flask import Flask, Blueprint, render_template, request
from flask_app.template_models.Index import Index
from suporte.Perguntar import Perguntar
from suporte.SupportFactory import SupportFactory
from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper
import markdown

web_framework = Flask(__name__)
route = Blueprint('route', __name__)
web_framework.register_blueprint(route)

@web_framework.route("/", endpoint="index", methods=['GET'])
def index():
    return render_template("index.html", view_model=Index())

@web_framework.route('/perguntar', endpoint="perguntar", methods=['POST'])
def perguntar():
    modelo = request.get_json().get('modelo')
    temperatura = request.get_json().get('temperatura')
    pergunta = request.get_json().get('pergunta')
    formato = request.get_json().get('formato', None)
    conveter_para_html = False
    if formato == "html":
        converter_para_html = True
    
    perguntar = Perguntar(
        SupportFactory.getLogger(), 
        Banco(), 
        GoogleApiWrapper(SupportFactory.buscar_chave_google())
    )
    resposta = perguntar.perguntar(pergunta, float(temperatura), modelo)
    if converter_para_html:
        resposta = markdown.markdown(resposta)
    
    return {
        "resposta": resposta
    }
