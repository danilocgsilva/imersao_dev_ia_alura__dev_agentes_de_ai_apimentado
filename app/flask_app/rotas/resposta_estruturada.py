from flask import Blueprint, render_template, request
from suporte.SupportFactory import SupportFactory
from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.Prompt import Prompt
from suporte.SupportFactory import SupportFactory
from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper
from flask_app.template_models.Prompt import Prompt as ModelPrompt

resposta_estruturada = Blueprint('resposta_estruturada', __name__)

@resposta_estruturada.route('/enviar_prompt', endpoint="enviar_prompt", methods=['POST'])
def enviar_prompt():
    prompt_usuario = request.get_json().get('prompt')
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
        prompt_usuario, 
        Banco(),
        GoogleApiWrapper(SupportFactory.buscar_chave_google()),
        modelo
    )
    
    resultado_prompt = prompt.triagemJson(pergunta)
    
    return {
        "resposta": resultado_prompt
    }
    
@resposta_estruturada.route("/prompt", endpoint="prompt", methods=['GET'])
def prompt():
    return render_template("prompt.html", view_model=ModelPrompt())