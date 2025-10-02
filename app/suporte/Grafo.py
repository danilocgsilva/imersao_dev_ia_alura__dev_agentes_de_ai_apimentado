from langgraph.graph import StateGraph, END, START
from suporte.AgentState import AgentState
from suporte.Prompt import Prompt
from suporte.Rag import Rag
from suporte.SupportFactory import SupportFactory
from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper

class Grafo:
    def __init__(self):
        self._logger = SupportFactory.getLogger()

    def buscar(self):
        workflow = StateGraph(AgentState)
        
        workflow.add_node("triagem", self._node_triagem)
        workflow.add_node("auto_resolver", self._node_auto_resolver)
        workflow.add_node("pedir_info", self._node_pedir_info)
        workflow.add_node("abrir_chamado", self._node_abrir_chamado)
        
        workflow.add_edge(START, "triagem")
        workflow.add_conditional_edges(
            "triagem",
            self._decidir_pos_triagem,
            {
                "auto": "auto_resolver",
                "info": "pedir_info",
                "chamado": "abrir_chamado"
            }
        )
        workflow.add_conditional_edges(
            "auto_resolver",
            self._decidir_pos_auto_resolver,
            {
                "info": "pedir_info",
                "chamado": "abrir_chamado",
                "ok": END
            }
        )
        
        workflow.add_edge("pedir_info", END)
        workflow.add_edge("auto_resolver", END)
        
        return workflow.compile()
        
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
        rag.setUp()
        resposta_rag = rag.perguntar_politica_rag(pergunta)
        
        update: AgentState = {
            "resposta": resposta_rag["answer"],
            "citacoes": resposta_rag.get("citacoes", []),
            "rag_sucesso": resposta_rag["contexto_encontrado"]
        }
        
        if resposta_rag["contexto_encontrado"]:
            update["acao_final"] = "AUTO_RESOLVER"
            
        return update

    def _node_pedir_info(self, state: AgentState) -> AgentState:
        print("Executando o nó de pedir informações...")
        faltantes = state["triagem"].get("campos_faltantes", [])
        if faltantes:
            detalhe = ",".join(faltantes)
        else:
            detalhe = "Tema e contexto específico"

        return {
            "resposta": f"Para avançar, preciso de detalhes: {detalhe}",
            "citacoes": [],
            "acao_final": "PEDIR_INFO"
        }
        
    def _node_abrir_chamado(self, state: AgentState) -> AgentState:
        print("Executando o nó de abrir chamado...")
        triagem = state["triagem"]
        
        return {
            "resposta": f"Abrindo chamado com urgência {triagem['urgencia']}. Descrição: {state['pergunta'][:140]}",
            "citacoe": [],
            "acao_final": "ABRIR_CHAMADO"
        }
        
    def _decidir_pos_triagem(self, state: AgentState) -> str:
        print("Decidindo pós triagem...")
        decisao = state["triagem"]["decisao"]
        
        if decisao == "AUTO_RESOLVER":
            return "auto"
        if decisao == "PEDIR_INFO":
            return "info"
        if decisao == "ABRIR_CHAMADO":
            return "chamado"
        
    def _decidir_pos_auto_resolver(self, state: AgentState) -> str:
        KEYWORDS_ABRIR_TICKET = ["aprovação", "exceção", "liberação", "abrir ticket", "abrir chamado", "acesso especial"]
        
        print("Decidindo após o auto_resolver...")
        
        if state["rag_sucesso"]:
            print("Rag com sucesso, finalizando o fluxo.")
            return "ok"
        
        state_da_pergunta = (state["pergunta"] or "").lower()
        
        if any(k in state_da_pergunta for k in KEYWORDS_ABRIR_TICKET):
            print("Rag falhou, mas foram encontradas keywords de abertura de ticket. Abrindo...")
            return "chamado"

        print("Rag falhou, sem keywords, vou pedir mais informações...")
        return "info"
    
    def _log(self, mensagem: str):
        self._logger.info(mensagem)
        
    def _triagem(self, pergunta: str):
        prompt = Prompt(
            SupportFactory.buscar_prompt_sistema_padrao(),
            Banco(),
            GoogleApiWrapper(SupportFactory.buscar_chave_google())
        )
        dados = prompt.triagem(pergunta)
        return dados["resposta"].model_dump()
    