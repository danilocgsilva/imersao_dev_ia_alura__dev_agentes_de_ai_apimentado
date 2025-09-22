from suporte.SupportFactory import SupportFactory
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.Banco import Banco
from suporte.Perguntar import Perguntar as PerguntarApp

class Perguntar:
    def __init__(self):
        self._logger = SupportFactory.getLogger()
        self._gaw = GoogleApiWrapper(SupportFactory.buscar_chave_google())
        self._resposta = ""
        self._pergunta = ""
        self._temperatura = 0.1
        
    def set_pergunta(self, pergunta: str):
        self._pergunta = pergunta
        
    def set_temperatura(self, temperatura: float):
        self._temperatura = temperatura
        
    def executar(self):
        if self._pergunta == "":
            raise Exception("A pergunta não foi feita. Use o método **set_pergunta** de **Comandos.Perguntar**")
        self._loginfo(f"Executando a pergunta: {self._pergunta}")
        print(f"Pergunta: {self._pergunta}")
        banco = Banco(self._logger)
        perguntar_app = PerguntarApp(self._logger, banco, self._gaw)
        self._resposta = perguntar_app.perguntar(self._pergunta, self._temperatura)
        
    def get_resposta(self) -> str:
        return self._resposta
        
    def _loginfo(self, mensagem):
        if self._logger:
            self._logger.info(mensagem)
