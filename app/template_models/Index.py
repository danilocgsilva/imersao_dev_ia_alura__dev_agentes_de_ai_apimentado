from ..suporte.Banco import Banco
from ..suporte.SupportFactory import SupportFactory

class Index:
    def __init__(self):
        self._titulo_pagina = "Faça uma pergunta"
        self._nome_app = "Faça uma pergunta"
        self._h1 = "Faça uma pergunta para a IA"
        self._lista_modelos = self._buscar_modelos()
        
    @property
    def titulo_pagina(self):
        return self._titulo_pagina
    
    @property
    def nome_app(self):
        return self._nome_app
    
    @property
    def h1(self):
        return self._h1
    
    @property
    def lista_modelos(self):
        # logger = SupportFactory.getLogger()
        # logger.info(self._lista_modelos)
        return self._lista_modelos
    
    def _buscar_modelos(self):
        banco = Banco()
        modelos = banco.listar_modelos_disponiveis()
        return modelos