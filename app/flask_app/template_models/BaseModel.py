class BaseModel:
    def __init__(self):
        self._titulo_pagina = ""
        self._nome_app = ""
        self._h1 = ""
        self._nome_pagina = ""
        self._javascript = ""
        self._nome_pagina_amigavel = ""
    
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
    def nome_pagina(self):
        return self._nome_pagina
    
    @property
    def nome_pagina_amigavel(self):
        return self._nome_pagina_amigavel
    
    @property
    def javascript(self):
        return self._javascript
    
    @property
    def stylesheets(self) -> list:
        return []
    