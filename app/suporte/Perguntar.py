from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper

class Perguntar:
    def __init__(self, logger, banco: Banco, gaw: GoogleApiWrapper):
        self._logger = logger
        self._banco = banco
        self._gaw = gaw
    
    def perguntar(self, pergunta: str):
        self._banco.registrar_pergunta(pergunta)
        resposta = self._gaw.buscar_resposta(pergunta)
        return resposta["resposta"].content