from suporte.Banco import Banco
from suporte.SupportFactory import SupportFactory
from flask_app.template_models.BaseModel import BaseModel
from flask import url_for, current_app
import os

class Rag(BaseModel):
    def __init__(self):
        super().__init__()
        self._titulo_pagina = "RAG"
        self._nome_app = "RAG"
        self._h1 = "RAG"
        self._lista_modelos = self._buscar_modelos()
        self._nome_pagina = "rag"
        self._nome_pagina_amigavel = "Rag"
        self._lista_perguntas_modelo = self._busca_perguntas_modelo()
        self._lista_arquivos_rag = self._busca_lista_arquivos_rag()
        self._javascripts = ["rag", "rag_drag_and_drop"]
        
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
    
    def _busca_lista_arquivos_rag(self):
        rag_path_fixos = os.path.join(current_app.root_path, 'documentos_rag', 'fixos')
        rag_path_dinamicos = os.path.join(current_app.root_path, 'documentos_rag', 'dinamicos')
        listagem_arquivos_fixos = os.listdir(rag_path_fixos)
        listagem_arquivos_dinamicos = os.listdir(rag_path_dinamicos)
        return listagem_arquivos_fixos + listagem_arquivos_dinamicos
    
    @property
    def lista_modelos(self):
        return self._lista_modelos
    
    @property
    def lista_perguntas_modelo(self):
        return self._lista_perguntas_modelo
    
    @property
    def lista_arquivos_rag(self):
        return self._lista_arquivos_rag
    
    @property
    def stylesheets(self) -> list:
        return [ 
            "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css",
            url_for('static', filename=self.nome_pagina) + '.css'
        ]
    