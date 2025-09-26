from suporte.Comandos.ComandoBase import ComandoBase
from suporte.Rag import Rag

class PerguntarComRag(ComandoBase):
    def __init__(self):
        super().__init__()
        self._pergunta = ""
        self._resposta = None
        
    def set_pergunta(self, pergunta: str):
        self._pergunta = pergunta
        
    def executar(self):
        rag = Rag()
        rag.setUp()
        self._resposta = rag.perguntar_politica_rag(self._pergunta)
        
    def get_resposta(self):
        return self._resposta
    