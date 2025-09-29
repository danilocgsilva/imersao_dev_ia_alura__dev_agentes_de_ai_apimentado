from suporte.Banco import Banco
from flask_app.template_models.BaseModel import BaseModel

class Index(BaseModel):
    def __init__(self):
        super().__init__()
        self._titulo_pagina = "Faça uma pergunta"
        self._nome_app = "Faça uma pergunta"
        self._h1 = "Faça uma pergunta para a IA"
        self._lista_modelos = self._buscar_modelos()
        self._nome_pagina = "perguntar"
        self._javascripts = ["perguntar"]
        self._nome_pagina_amigavel = "Faça uma pergunta"
        
    @property
    def lista_modelos(self):
        return self._lista_modelos
    
    def _buscar_modelos(self):
        banco = Banco()
        modelos = banco.listar_modelos_disponiveis()
        if modelos == None:
            return []
        return modelos
    