from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.DadosDesempenho import DadosDesempenho

class Perguntar:
    def __init__(self, logger, banco: Banco, gaw: GoogleApiWrapper):
        self._logger = logger
        self._banco = banco
        self._gaw = gaw
    
    def perguntar(self, pergunta: str, temperatura: float = 0.1, modelo: str = "gemini-2.5-flash") -> str:
        dados: dict = self._gaw.buscar_resposta(pergunta, temperatura, modelo)
        resposta = dados["resposta"]
        resposta_str = resposta.content
        
        self._banco.registrar_pergunta(pergunta)
        id_pergunta = self._banco.ultimo_id_inserido
        self._banco.registrar_resposta(
            resposta_str, 
            id_pergunta, 
            dados["timestamp_antes"],
            dados["timestamp_depois"],
            dados["diferenca_ms"],
        )
        self._banco.registrar_request(resposta, dados["comando"])
        
        return resposta_str