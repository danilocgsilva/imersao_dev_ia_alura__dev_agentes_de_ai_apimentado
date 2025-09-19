import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
        
class GoogleApiWrapper:
    def __init__(self, chave_google):
        self._chave_google = chave_google
    
    def getModels(self) -> list:
        genai.configure(api_key=self._chave_google)
        response = genai.list_models()
        return list(response)
    
    def getLLM(self) -> ChatGoogleGenerativeAI:
        llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash", 
            google_api_key=self._chave_google,
            temperature=0.1
        )
        return llm
    
    def buscar_resposta(self, pergunta: str):
        llm = self.getLLM()
        return {
            "resposta": llm.invoke(pergunta),
            "comando": "ChatGoogleGenerativeAI().invoke(<pergunta>)"
        }
        