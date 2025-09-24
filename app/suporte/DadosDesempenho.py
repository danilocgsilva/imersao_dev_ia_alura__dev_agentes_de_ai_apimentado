import time
from suporte.TriagemOut import TriagemOut
from langchain_core.messages import HumanMessage, SystemMessage

class DadosDesempenho:
    def __init__(
        self, 
        llm, 
        temperatura: float, 
        modelo: str, 
        system_prompt: str = ""
    ):
        self._llm = llm
        self._temperatura = temperatura
        self._modelo = modelo
        self._system_prompt = system_prompt
    
    def invoke(self, pergunta: str):
        timestamp_antes = time.time_ns()
        
        resposta = None
        if self._system_prompt == "":
            resposta = self._llm.invoke(pergunta)
        else:
            cadeia_triagem = self._llm.with_structured_output(TriagemOut)
            
            resposta: TriagemOut = cadeia_triagem.invoke([
                SystemMessage(content=self._system_prompt),
                HumanMessage(content=pergunta)
            ])
        
        timestamp_depois = time.time_ns()
        diferenca_ms = (timestamp_depois - timestamp_antes) / 1_000_000

        return {
            "resposta": resposta,
            "temperatura": self._temperatura,
            "modelo_utilizado": self._modelo,
            "comando": "ChatGoogleGenerativeAI().invoke(<pergunta>)",
            "timestamp_antes": timestamp_antes / 1000000,
            "timestamp_depois": timestamp_depois / 1000000,
            "diferenca_ms": diferenca_ms
        }