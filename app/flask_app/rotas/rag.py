from flask import Blueprint, render_template, request, send_from_directory, abort
from suporte.Banco import Banco
from flask_app.template_models.Rag import Rag
from suporte.Rag import Rag as RagDomain
from suporte.ContarDesempenhoPergunta import ContarDesempenhoPergunta
from suporte.SupportFactory import SupportFactory
import os

rag = Blueprint('rag', __name__)

@rag.route('/rag', endpoint="rag", methods=['GET'])
def rag_view():
    return render_template("rag.html", view_model=Rag())

@rag.route('/rag_enviar', endpoint="rag_enviar", methods=['POST'])
def rag_enviar():
    pergunta = request.get_json().get('pergunta')
    
    rad_domain = RagDomain()
    contar_desempenho_pergunta = ContarDesempenhoPergunta(rad_domain)
    contar_desempenho_pergunta.pergunta = pergunta
    contar_desempenho_pergunta.executar()
    
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

@rag.route('/rag/download/<filename>', endpoint="download_documento_rag", methods=['GET'])
def download_arquivo_rag(filename):
    try:
        if '..' in filename or filename.startswith('/'):
            abort(400)
            
        documentos_path = os.path.join(os.path.dirname(__file__), '..', 'documentos_rag', 'fixos')
        if not os.path.exists(os.path.join(documentos_path, filename)):
            abort(404)
        return send_from_directory(documentos_path, filename)
    except Exception as e:
        logger = SupportFactory.getLogger()
        logger.error(f"Erro ao baixar o arquivo {filename}: {e}")
        abort(500)


