import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
import time
        
class GoogleApiWrapper:
    def __init__(self, chave_google):
        self._chave_google = chave_google
        self._modelo_padrao = "gemini-2.5-flash"
    
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
    
    def buscar_resposta(self, pergunta: str, temperatura: float = 0.1, modelo: str = "gemini-2.5-flash"):
        llm = self.getLLM(temperatura)
        
        timestamp_antes = time.time_ns()
        resposta = llm.invoke(pergunta)
        timestamp_depois = time.time_ns()
        diferenca_ms = (timestamp_depois - timestamp_antes) / 1_000_000

        return {
            "resposta": resposta,
            "temperatura": temperatura,
            "modelo_utilizado": modelo,
            "comando": "ChatGoogleGenerativeAI().invoke(<pergunta>)",
            "timestamp_antes": timestamp_antes / 1000000,
            "timestamp_depois": timestamp_depois / 1000000,
            "diferenca_ms": diferenca_ms
        }
        