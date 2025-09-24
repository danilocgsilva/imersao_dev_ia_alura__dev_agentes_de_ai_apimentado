from suporte.TriagemOut import TriagemOut
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.SupportFactory import SupportFactory
from langchain_core.messages import HumanMessage, SystemMessage
from typing import Literal, List, Dict
import json
from suporte.DadosDesempenho import DadosDesempenho
from google_api.GoogleApiWrapper import GoogleApiWrapper

class Prompt:
    def __init__(
        self, 
        system_prompt, 
        gaw: GoogleApiWrapper,
        modelo: str = "gemini-2.5-flash",
        temperatura: float = 0.1
    ):
        self._system_prompt = system_prompt
        self._modelo = modelo
        self._gaw = gaw
        self._temperatura = temperatura
        
    def triagemJson(self, mensagem_humana: str):
        dados = self.triagem(mensagem_humana)
        
        resultados = dados["resposta"].model_dump()
        resultadosJson = json.dumps(resultados, indent=10)
        return self.newlineParaBr(resultadosJson)
    
    def triagem(self, mensagem_humana: str) -> dict:
        dados: dict = self._gaw.buscar_resposta(
            mensagem_humana,
            self._temperatura,
            system_prompt = self._system_prompt
        )
        return dados
    
    def get_triagem_chain(self):
        gaw = GoogleApiWrapper(SupportFactory.buscar_chave_google())
        llm_triagem = gaw.getLLM(modelo = self._modelo)
        triagem_chain = llm_triagem.with_structured_output(TriagemOut)
        return triagem_chain
    
    def newlineParaBr(self, conteudo: str):
        return conteudo.replace('\n', '<br>')        
    