import logging
import uuid
import os

class SupportFactory:
    @staticmethod
    def getLogger(identificador: str = None):
        if not identificador:
            identificador = str(uuid.uuid4())
        logging.getLogger().setLevel(logging.DEBUG)

        file_handler = logging.FileHandler("app.log")
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        logger = logging.getLogger(identificador)
        logger.addHandler(file_handler)
        file_handler.setFormatter(formatter)

        return logger
    
    @staticmethod
    def buscar_chave_google() -> str:
        return os.environ.get("CHAVE_API_GOOGLE")
    
    @staticmethod
    def buscar_prompt_sistema_padrao() -> str:
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
    