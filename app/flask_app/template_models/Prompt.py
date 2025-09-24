from suporte.Banco import Banco
from suporte.SupportFactory import SupportFactory

class Prompt:
    def __init__(self):
        self._titulo_pagina = "Prompt"
        self._nome_app = "Pergunta com prompt"
        self._h1 = "Prepare um prompt"
        self._lista_modelos = self._buscar_modelos()
        self._nome_pagina = "prompt"
        self._javascript = "prompt"
        self._nome_pagina_amigavel = "Prompt"
        self._lista_perguntas_modelo = self._busca_perguntas_modelo()
        
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
    def perguntas_modelo(self):
        return self._lista_perguntas_modelo
    
    @property
    def javascript(self):
        return self._javascript
    
    @property
    def prompt(self):
        prompt = """
Você é um triador de Service Desk para políticas internas da empresa Carraro Desenvolvimento. 
Dada a mensagem do usuário, retorne SOMENTE um JSON com:
{
    "decisao": "AUTO_RESOLVER" | "PEDIR_INFO" | "ABRIR_CHAMADO",
    "urgencia": "BAIXA" | "MEDIA" | "ALTA",
    "campos_faltantes": ["..."]
}
Regras:
- **AUTO_RESOLVER**: Perguntas claras sobre regras ou procedimentos descritos nas políticas (Ex: "Posso reembolsar a internet do meu home office?", "Como funciona a política de alimentação em viagens?").
- **PEDIR_INFO**: Mensagens vagas ou que faltam informações para identificar o tema ou contexto (Ex: "Preciso de ajuda com uma política", "Tenho uma dúvida geral").
- **ABRIR_CHAMADO**: Pedidos de exceção, liberação, aprovação ou acesso especial, ou quando o usuário explicitamente pede para abrir um chamado (Ex: "Quero exceção para trabalhar 5 dias remoto.", "Solicito liberação para anexos externos.", "Por favor, abra um chamado para o RH.").
Analise a mensagem e decida a ação mais apropriada.
"""
        return prompt
    
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
