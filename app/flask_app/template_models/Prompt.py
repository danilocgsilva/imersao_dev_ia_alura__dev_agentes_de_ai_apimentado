from suporte.Banco import Banco
from suporte.SupportFactory import SupportFactory
from flask_app.template_models.BaseModel import BaseModel

class Prompt(BaseModel):
    def __init__(self):
        super().__init__()
        self._titulo_pagina = "Resposta Estruturada"
        self._nome_app = "Pergunta com prompt"
        self._h1 = "Prepare um prompt"
        self._lista_modelos = self._buscar_modelos()
        self._nome_pagina = "prompt"
        self._javascript = "prompt"
        self._nome_pagina_amigavel = "Resposta estruturada"
        self._lista_perguntas_modelo = self._busca_perguntas_modelo()
        
    @property
    def lista_modelos(self):
        return self._lista_modelos
    
    @property
    def perguntas_modelo(self):
        return self._lista_perguntas_modelo
    
    @property
    def prompt(self):
        return SupportFactory.buscar_prompt_sistema_padrao()
    
    def _buscar_modelos(self):
        banco = Banco()
        modelos = banco.listar_modelos_disponiveis()
        
        if modelos == None:
            return []
        return modelos
    
    def _busca_perguntas_modelo(self):
        banco = Banco()
        perguntas = banco.listar_perguntas_modelo()
        if perguntas == None:
            return []
        return perguntas
