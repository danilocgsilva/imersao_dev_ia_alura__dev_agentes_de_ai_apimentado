import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from suporte.DadosDesempenho import DadosDesempenho
import time
        
class GoogleApiWrapper:
    def __init__(self, chave_google):
        self._chave_google = chave_google
        self._modelo_padrao = "gemini-2.5-flash"
        self._temperatura = 0.1
    
    def getModels(self) -> list:
        genai.configure(api_key=self._chave_google)
        response = genai.list_models()
        return list(response)
    
    def getLLM(self, temperatura: float = 0.1, modelo: str = None) -> ChatGoogleGenerativeAI:
        if modelo == None:
            modelo = self._modelo_padrao
        
        llm = ChatGoogleGenerativeAI(
            model=modelo, 
            google_api_key=self._chave_google,
            temperature=temperatura
        )
        return llm     
    
    def buscar_resposta(
        self, 
        pergunta: str, 
        temperatura: float = 0.1, 
        modelo: str = "gemini-2.5-flash",
        system_prompt: str = ""
    ):
        llm = self.getLLM(temperatura)
        
        dados_desempenho = DadosDesempenho(
            llm,
            temperatura,
            modelo,
            system_prompt
        )
        
        return dados_desempenho.invoke(pergunta)
