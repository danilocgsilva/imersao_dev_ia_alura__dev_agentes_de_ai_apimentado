from flask import Flask, Blueprint, render_template, request, url_for, redirect
from flask_app.template_models.Index import Index
from flask_app.template_models.Prompt import Prompt as ModelPrompt
from flask_app.template_models.Rag import Rag
from suporte.Perguntar import Perguntar
from suporte.SupportFactory import SupportFactory
from suporte.Banco import Banco
from suporte.Prompt import Prompt
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
    return render_template("prompt.html", view_model=ModelPrompt())

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
    pergunta_modelo = request.get_json().get('pergunta_modelo')
    tipo_pergunta = request.get_json().get('tipo_pergunta')
    pergunta_aberta = request.get_json().get('pergunta_aberta')
    
    pergunta = ""
    if tipo_pergunta == "pergunta_aberta":
        pergunta = pergunta_aberta
    elif tipo_pergunta == "pergunta_modelo":
        pergunta = pergunta_modelo
        
    prompt = Prompt(
        prompt, 
        Banco(),
        GoogleApiWrapper(SupportFactory.buscar_chave_google()),
        modelo
    )
        
    resultado_prompt = prompt.triagemJson(pergunta)

    return {
        "resposta": resultado_prompt
    }
    
@web_framework.route('/rag', endpoint="rag", methods=['GET'])
def rag():
    return render_template("rag.html", view_model=Rag())
