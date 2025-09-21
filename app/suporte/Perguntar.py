from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper

class Perguntar:
    def __init__(self, logger, banco: Banco, gaw: GoogleApiWrapper):
        self._logger = logger
        self._banco = banco
        self._gaw = gaw
    
    def perguntar(self, pergunta: str, temperatura: float = 0.1, modelo: str = "gemini-2.5-flash") -> str:
        resposta_gaw = self._gaw.buscar_resposta(pergunta, temperatura, modelo)
        resposta = resposta_gaw["resposta"]
        resposta_str = resposta.content
        
        print(resposta_gaw)
        
        self._banco.registrar_pergunta(pergunta)
        id_pergunta = self._banco.ultimo_id_inserido
        self._banco.registrar_resposta(
            resposta_str, 
            id_pergunta, 
            resposta, 
            resposta_gaw["temperatura"], 
            resposta_gaw["modelo_utilizado"],
            resposta_gaw["timestamp_antes"],
            resposta_gaw["timestamp_depois"],
            resposta_gaw["diferenca_ms"],
        )
        self._banco.registrar_request(resposta, resposta_gaw["comando"])
        
        return resposta_str