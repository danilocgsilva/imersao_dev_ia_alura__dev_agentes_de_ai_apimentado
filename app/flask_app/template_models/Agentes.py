from flask_app.template_models.BaseModel import BaseModel

class Agentes(BaseModel):
    def __init__(self):
        super().__init__()
        self._titulo_pagina = "Agentes"
        self._nome_app = "Ativação de agentes"
        self._h1 = "Agentes"
        self._nome_pagina = "Agentes"
        self._javascripts = []
        self._nome_pagina_amigavel = "Agentes"
    