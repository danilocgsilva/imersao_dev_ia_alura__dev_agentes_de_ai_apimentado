from suporte.TriagemOut import TriagemOut
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.SupportFactory import SupportFactory
import json
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.Banco import Banco

class Prompt:
    def __init__(
        self, 
        system_prompt, 
        banco: Banco,
        gaw: GoogleApiWrapper,
        modelo: str = "gemini-2.5-flash",
        temperatura: float = 0.1
    ):
        self._system_prompt = system_prompt
        self._banco = banco
        self._modelo = modelo
        self._gaw = gaw
        self._temperatura = temperatura
        
    def triagemJson(self, mensagem_humana: str):
        dados = self.triagem(mensagem_humana)
        
        resultados = dados["resposta"].model_dump()
        
        resultadosJson = json.dumps(resultados, indent=10)
        
        self._banco.registrar_pergunta(mensagem_humana)
        id_pergunta = self._banco.ultimo_id_inserido
        self._banco.registrar_resposta(
            resultadosJson, 
            id_pergunta, 
            resultados, 
            dados["temperatura"], 
            dados["modelo_utilizado"],
            dados["timestamp_antes"],
            dados["timestamp_depois"],
            dados["diferenca_ms"],
        )
        self._banco.registrar_request(resultadosJson, dados["comando"])
        
        
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
    