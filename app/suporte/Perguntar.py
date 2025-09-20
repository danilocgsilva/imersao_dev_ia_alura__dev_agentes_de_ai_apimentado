from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper

class Perguntar:
    def __init__(self, logger, banco: Banco, gaw: GoogleApiWrapper):
        self._logger = logger
        self._banco = banco
        self._gaw = gaw
    
    def perguntar(self, pergunta: str, temperatura: float = 0.1) -> str:
        resposta_gaw = self._gaw.buscar_resposta(pergunta, temperatura)
        resposta = resposta_gaw["resposta"]
        resposta_str = resposta.content
        
        self._banco.registrar_pergunta(pergunta)
        id_pergunta = self._banco.ultimo_id_inserido
        self._banco.registrar_resposta(resposta_str, id_pergunta, resposta)
        self._banco.registrar_request(resposta, resposta_gaw["comando"])
        
        return resposta_str