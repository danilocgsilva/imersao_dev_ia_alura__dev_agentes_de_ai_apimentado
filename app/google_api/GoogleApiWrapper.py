import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from suporte.DadosDesempenho import DadosDesempenho
from suporte.DesempenhoApi import DesempenhoApi
from suporte.Banco import Banco
        
class GoogleApiWrapper:
    def __init__(self, chave_google):
        self._chave_google = chave_google
        self._modelo_padrao = "gemini-2.5-flash"
        self._temperatura = 0.1
        self._pergunta = None
        self._modelo = None
        self._system_prompt = None
        
    @property
    def pergunta(self) -> str:
        return self._pergunta
    
    @pergunta.setter
    def pergunta(self, pergunta: str):
        self._pergunta = pergunta
    
    @property
    def temperatura(self) -> float:
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, temperatura: float):
        self._temperatura = temperatura
    
    @property
    def modelo(self) -> str:
        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo: str):
        self._modelo = modelo
    
    @property
    def system_prompt(self) -> str:
        return self._system_prompt
    
    @system_prompt.setter
    def system_prompt(self, system_prompt: str):
        self._system_prompt = system_prompt
    
    def getModels(self, banco: Banco = None) -> list:
        genai.configure(api_key=self._chave_google)
        
        if banco:
            desempenho_api = DesempenhoApi(genai)
            desempenho_api.executar("google.generativeai.list_models()")
            desempenho_api.registrar(banco, "Busca de modelos disponíveis")
            response = desempenho_api.buscar_resultado()
        else:
            response = genai.list_models()
        
        return list(response)
    
    def getLLM(self, temperatura: float = 0.1, modelo: str = None) -> ChatGoogleGenerativeAI:
        if modelo is not None:
            self._modelo = modelo
            
        if temperatura is not None:
            self._temperatura = temperatura
            
        llm = ChatGoogleGenerativeAI(
            model=self._modelo, 
            google_api_key=self._chave_google,
            temperature=self._temperatura
        )
        return llm     
    
    def buscar_resposta(
        self, 
        pergunta: str = None, 
        temperatura: float = None, 
        modelo: str = None,
        system_prompt: str = None
    ):
        if temperatura is not None:
            self._temperatura = temperatura
            
        if pergunta is not None:
            self._pergunta = pergunta
            
        if modelo is not None:
            self._modelo = modelo
        else:
            self._modelo = self._modelo_padrao
        
        if system_prompt is not None:
            self._system_prompt = system_prompt
            
            
        print("----")
        print(self._temperatura)
        print(self._pergunta)
        print(self._modelo)
        print(self._system_prompt)
        print("----")
        
        # raise Exception("Parada 13")
            
        llm = self.getLLM(temperatura)
        
        dados_desempenho = DadosDesempenho(
            llm,
            self._temperatura,
            self._modelo,
            self._system_prompt
        )
        
        return dados_desempenho.invoke(self._pergunta)
