class ContarDesempenhoPergunta:
    def __init__(self, objeto_dominio):
        self._objeto_dominio = objeto_dominio
        self._pergunta = ""
        self._resposta = ""
        
    @property
    def pergunta(self) -> str:
        return self._pergunta
    
    @pergunta.setter
    def pergunta(self, pergunta: str):
        self._pergunta = pergunta
        
    def executar(self):
        if self._pergunta == "":
            raise Exception("A pergunta não foi definida.")
        
        if type(self._objeto_dominio).__name__ == "Rag":
            self._objeto_dominio.setUp()
            resposta_raw = self._objeto_dominio.perguntar_politica_rag(self._pergunta)
            self._resposta = resposta_raw["answer"]
        else:
            raise Exception("O objeto de domínio não é reconhecido.")
        
    def buscar_resposta(self) -> str:
        return self._resposta
    