from flask import Flask, Blueprint, render_template, request, url_for, redirect
from flask_app.template_models.Index import Index
from flask_app.template_models.Prompt import Prompt
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
    return redirect(url_for("perguntar"))

@web_framework.route("/perguntar", endpoint="perguntar", methods=['GET'])
def perguntar():
    return render_template("perguntar.html", view_model=Index())

@web_framework.route("/prompt", endpoint="prompt", methods=['GET'])
def prompt():
    return render_template("prompt.html", view_model=Prompt())

@web_framework.route('/enviar_pergunta', endpoint="enviar_pergunta", methods=['POST'])
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
    
@web_framework.route('/enviar_prompt', endpoint="enviar_prompt", methods=['POST'])
def enviar_prompt():
    prompt = request.get_json().get('prompt')
    modelo = request.get_json().get('modelo')
    # temperatura = request.get_json().get('temperatura')
    # formato = request.get_json().get('formato', None)

    # converter_para_html = False
    # if formato == "html":
    #     converter_para_html = True

    # perguntar = Perguntar(
    #     SupportFactory.getLogger(),
    #     Banco(),
    #     GoogleApiWrapper(SupportFactory.buscar_chave_google())
    # )
    # resposta = perguntar.perguntar(prompt, float(temperatura), modelo)
    # if converter_para_html:
    #     resposta = markdown.markdown(resposta)

    return {
        "resposta": "teste teste"
    }
