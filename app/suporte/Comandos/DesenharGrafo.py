from suporte.Comandos.ComandoBase import ComandoBase
from typing import TypeDict, Optional
from suporte.AgentState import AgentState
from suporte.SupportFactory import SupportFactory
from suporte.Prompt import Prompt
from suporte.Rag import Rag

class DesenharGrafo(ComandoBase):
    def __init__(self):
        self._logger = SupportFactory.getLogger()
    
    def executar(self):
        print("Executar")
        
    def _node_triagem(self, state: AgentState) -> AgentState:
        self._log("Executando o nó de triagem...")
        pergunta = state["pergunta"]
        return {
            "triagem": self._triagem(pergunta)
        }
    
    def _node_auto_resolver(self, state: AgentState) -> AgentState:
        print("Executando o nó de auto resolver...")
        pergunta = state["pergunta"]
        rag = Rag()
        resposta_rag = rag.perguntar_politica_rag(pergunta)
        
        update: AgentState = {
            "resposta": resposta_rag["answer"],
            "citacoes": resposta_rag.get("citacoes", []),
            "rag_sucesso": resposta_rag["contexto_encontrado"]
        }
        
        if resposta_rag["contexto_encontrado"]:
            update["acao_final"] = "AUTO_RESOLVER"
            
        return update
    
    def _log(self, mensagem: str):
        self._logger.info(mensagem)
        
    def _triagem(self, pergunta: str):
        prompt = Prompt()
        dados = prompt.triagem(pergunta)
        return dados["resposta"].model_dump()
            
    