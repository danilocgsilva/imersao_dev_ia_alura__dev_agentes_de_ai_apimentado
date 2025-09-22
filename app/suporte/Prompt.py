from suporte.TriagemOut import TriagemOut
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.SupportFactory import SupportFactory
from langchain_core.messages import HumanMessage, SystemMessage
from typing import Literal, List, Dict
from langchain_google_genai import ChatGoogleGenerativeAI

class Prompt:
    def __init__(self, system_prompt):
        self._system_prompt = system_prompt
    
    def triagem(self, mensagem_humana: str) -> Dict:
        saida: TriagemOut = self.get_triagem_chain().invoke([
            SystemMessage(content=self._system_prompt),
            HumanMessage(content=mensagem_humana)
        ])
        
        return saida.model_dump()
    
    def get_triagem_chain(self):
        gaw = GoogleApiWrapper(SupportFactory.buscar_chave_google())
        llm_triagem = gaw.getLLM()
        triagem_chain = llm_triagem.with_structured_output(TriagemOut)
        return triagem_chain
    
    def testes(self):
        testes = [
            "Posso reembolsar a internet?",
            "Quero mais 5 dias de trabalho remoto. Como faço?",
            "Posso reembolsar cursos ou treinamentos da Alura",
            "Quantas capivaras tem no rio Pinheiros?"
        ]