from suporte.TriagemOut import TriagemOut
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.SupportFactory import SupportFactory
from langchain_core.messages import HumanMessage, SystemMessage
from typing import Literal, List, Dict
import json

class Prompt:
    def __init__(self, system_prompt, modelo: str = None):
        self._system_prompt = system_prompt
        self._modelo = modelo
    
    def triagem(self, mensagem_humana: str) -> Dict:
        saida: TriagemOut = self.get_triagem_chain().invoke([
            SystemMessage(content=self._system_prompt),
            HumanMessage(content=mensagem_humana)
        ])
        
        return saida.model_dump()
    
    def triagemJson(self, mensagem_humana: str):
        resultados = self.triagem(mensagem_humana)
        resultadosJson = json.dumps(resultados, indent=10)
        return self.newlineParaBr(resultadosJson)
    
    def get_triagem_chain(self):
        gaw = GoogleApiWrapper(SupportFactory.buscar_chave_google())
        llm_triagem = gaw.getLLM(modelo = self._modelo)
        triagem_chain = llm_triagem.with_structured_output(TriagemOut)
        return triagem_chain
    
    def newlineParaBr(self, conteudo: str):
        return conteudo.replace('\n', '<br>')        
    