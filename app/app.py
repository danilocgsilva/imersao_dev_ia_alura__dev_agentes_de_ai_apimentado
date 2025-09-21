from flask import Flask, Blueprint, render_template, request
from .template_models.Index import Index
from .suporte.Perguntar import Perguntar
from .suporte.SupportFactory import SupportFactory
from .suporte.Banco import Banco
from .google_api.GoogleApiWrapper import GoogleApiWrapper

app = Flask(__name__)
route = Blueprint('route', __name__)
app.register_blueprint(route)

@app.route("/", endpoint="index", methods=['GET'])
def index():
    return render_template("index.html", view_model=Index())

@app.route('/perguntar', endpoint="perguntar", methods=['POST'])
def perguntar():
    modelo = request.get_json().get('modelo')
    temperatura = request.get_json().get('temperatura')
    pergunta = request.get_json().get('pergunta')
    
    perguntar = Perguntar(
        SupportFactory.getLogger(), 
        Banco(), 
        GoogleApiWrapper(SupportFactory.buscar_chave_google())
    )
    resposta = perguntar.perguntar(pergunta, float(temperatura), modelo)
    
    return {
        "resposta": resposta
    }
