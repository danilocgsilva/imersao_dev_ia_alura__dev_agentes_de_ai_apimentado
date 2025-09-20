import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
        
class GoogleApiWrapper:
    def __init__(self, chave_google):
        self._chave_google = chave_google
    
    def getModels(self) -> list:
        genai.configure(api_key=self._chave_google)
        response = genai.list_models()
        return list(response)
    
    def getLLM(self, temperatura: float = 0.1, modelo: str = "gemini-2.5-flash") -> ChatGoogleGenerativeAI:
        llm = ChatGoogleGenerativeAI(
            model=modelo, 
            google_api_key=self._chave_google,
            temperature=temperatura
        )
        return llm
    
    def buscar_resposta(self, pergunta: str, temperatura: float = 0.1, modelo: str = "gemini-2.5-flash"):
        llm = self.getLLM(temperatura)
        return {
            "resposta": llm.invoke(pergunta),
            "temperatura": temperatura,
            "modelo_utilizado": modelo,
            "comando": "ChatGoogleGenerativeAI().invoke(<pergunta>)"
        }
        