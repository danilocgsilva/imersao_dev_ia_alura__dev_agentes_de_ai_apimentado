class ArquivoRag:
    def __init__(self, arquivo: str, fixo: bool):
        self._nome = arquivo
        self._fixo = fixo
        
    @property
    def nome(self) -> str:
        return self._nome
    
    @property
    def fixo(self) -> bool:
        return self._fixo