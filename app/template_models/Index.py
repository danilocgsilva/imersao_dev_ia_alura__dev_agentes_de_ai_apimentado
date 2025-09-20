class Index:
    def __init__(self):
        self._titulo_pagina = "Faça uma pergunta"
        self._nome_app = "Faça uma pergunta"
        self._h1 = "Faça uma pergunta para a IA"
        
    @property
    def titulo_pagina(self):
        return self._titulo_pagina
    
    @property
    def nome_app(self):
        return self._nome_app
    
    @property
    def h1(self):
        return self._h1