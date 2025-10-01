from typing import TypeDict, Optinal, List

class AgentState(TypeDict, total = False):
    pergunta: str
    triagem: dict
    resposta: Optinal[str]
    citacoes: List[dict]
    rag_sucesso: bool
    acao_final: str
    