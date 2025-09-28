import time
from suporte.SupportFactory import SupportFactory

class ContarDesempenhoPergunta:
    def __init__(self, objeto_dominio):
        self._objeto_dominio = objeto_dominio
        self._pergunta = ""
        self._resposta = ""
        self._raw_resposta = None
        self._temperatura = None
        self._comando = ""
        self._timestamp_inicio = None
        self._timestamp_final = None
        self._tempo_transcorrido = None
        self._logger = SupportFactory.getLogger()
        
    @property
    def temperatura(self) -> float:
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, temperatura: float):
        self._temperatura = temperatura
        
    @property
    def comando(self) -> str:
        return self._comando
    
    @comando.setter
    def comando(self, comando: str):
        self._comando = comando
        
    @property
    def pergunta(self) -> str:
        return self._pergunta
    
    @pergunta.setter
    def pergunta(self, pergunta: str):
        self._pergunta = pergunta
        
    @property
    def resposta(self) -> str:
        return self._resposta
    
    @property
    def raw_resposta(self):
        return self._raw_resposta
        
    def executar(self):
        if self._pergunta == "":
            raise Exception("A pergunta não foi definida.")
        
        self._timestamp_inicio = time.time_ns()
        if type(self._objeto_dominio).__name__ == "Rag":
            self._objeto_dominio.setUp()
            self._raw_resposta = self._objeto_dominio.perguntar_politica_rag(self._pergunta)
            self._resposta = self._raw_resposta["answer"]
            self._escrever_dados_pergunta_log()
        else:
            raise Exception("O objeto de domínio não é reconhecido.")
        self._timestamp_final = time.time_ns()
        self._tempo_transcorrido = (self._timestamp_final - self._timestamp_inicio) / 1_000_000
        
    def buscar_resposta(self) -> str:
        return self._resposta
    
    def _escrever_dados_pergunta_log(self):
        pergunta_string = f"PERGUNTA: {self._pergunta}"
        resposta_string = f"RESPOSTA: {self._raw_resposta['answer']}"
        citacoes = f"CITAÇÕES: {self._raw_resposta['citacoes']}"
        self._logger.info("-" * 30)
        self._logger.info(pergunta_string)
        self._logger.info(resposta_string)
        self._logger.info(citacoes)
    
    @property
    def dados_desempenho(self):
        base_dictionary = {
            "resposta": self._raw_resposta,
            "comando": self._comando,
            "timestamp_antes": self._timestamp_inicio / 1000000,
            "timestamp_depois": self._timestamp_final / 1000000,
            "diferenca_ms": self._tempo_transcorrido
        }
        
        dictionary = base_dictionary
        
        if self._temperatura is not None:
            dictionary["temperatura"] = self._temperatura
        
        return dictionary