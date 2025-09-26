from flask import Blueprint, render_template, request
from flask_app.template_models.Index import Index
import markdown
from suporte.Perguntar import Perguntar
from suporte.SupportFactory import SupportFactory
from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper

pergunta_simples = Blueprint('pergunta_simples', __name__)

@pergunta_simples.route("/")
def mainroute():
    return "Hello! I am a working route!"

@pergunta_simples.route("/perguntar", endpoint="perguntar", methods=['GET'])
def perguntar():
    return render_template("perguntar.html", view_model=Index())

@pergunta_simples.route('/enviar_pergunta', endpoint="enviar_pergunta", methods=['POST'])
def enviar_pergunta():
    modelo = request.get_json().get('modelo')
    temperatura = request.get_json().get('temperatura')
    pergunta = request.get_json().get('pergunta')
    formato = request.get_json().get('formato', None)
    
    converter_para_html = False
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