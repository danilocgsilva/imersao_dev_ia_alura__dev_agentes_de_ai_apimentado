from suporte.Banco import Banco

class Rag:
    def __init__(self):
        self._titulo_pagina = "RAG"
        self._nome_app = "RAG"
        self._h1 = "RAG"
        self._lista_modelos = self._buscar_modelos()
        self._nome_pagina = "rag"
        self._nome_pagina_amigavel = "Rag"
        self._lista_perguntas_modelo = self._busca_perguntas_modelo()
        
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
        return self._lista_modelos
    
    @property
    def nome_pagina(self):
        return self._nome_pagina
    
    @property
    def nome_pagina_amigavel(self):
        return self._nome_pagina_amigavel
    
    @property
    def lista_perguntas_modelo(self):
        return self._lista_perguntas_modelo
    
    @property
    def javascript(self):
        return None

    