import time
from suporte.Banco import Banco
from suporte.Utilidades import Utilidades

class DesempenhoApi:
    def __init__(self, objeto_dominio):
        self._objeto_dominio = objeto_dominio
        self._timestamp_inicio = None
        self._timestamp_final = None
        self._tempo_transcorrido = None
        self._response = None
        self._definidor = None
        self._contexto = None
        self._id_desempenho_api = None
        self._modelo = None
        
    @property
    def modelo(self) -> str:
        return self._modelo

    @modelo.setter
    def modelo(self, modelo: str):
        self._modelo = modelo
        
    def registrar(self, banco: Banco, contexto: str):
        self._contexto = contexto
        
        if type(self._response).__name__ == "generator":
            self._response = list(self._response)
        
        banco.registrar_desempenho_api(
            self._contexto,
            self._timestamp_inicio,
            self._timestamp_final,
            self._tempo_transcorrido,
            self._definidor,
            Utilidades.serializar(self._response)
        )
        self._id_desempenho_api = banco.ultimo_id_inserido
        if self._definidor == "GoogleApiWrapper.buscar_resposta()":
            banco.registrar_modelo_utilizado_api(self._modelo, self._id_desempenho_api)
        
    def executar(self, definidor: str):
        definidores_esperados = {
            "google.generativeai.list_models()",
            "GoogleApiWrapper.buscar_resposta()"
        }
        if definidor not in definidores_esperados:
            raise Exception("O objeto de domínio não é reconhecido.")
        self._definidor = definidor

        self._timestamp_inicio = time.time_ns() / 1_000_000

        if definidor == "google.generativeai.list_models()":
            self._genai_list_models()
        if definidor == "GoogleApiWrapper.buscar_resposta()":
            if self._modelo == None:
                raise Exception("O modelo não foi definido.")
            self._googe_api_wrapper_buscar_resposta()
            
        self._timestamp_final = time.time_ns() / 1_000_000
        self._tempo_transcorrido = self._timestamp_final - self._timestamp_inicio
        
    def buscar_resultado(self) -> str:
        return self._response
    
    def _genai_list_models(self):
        self._response = self._objeto_dominio.list_models()
        
    def _googe_api_wrapper_buscar_resposta(self):
        self._response = self._objeto_dominio.buscar_resposta()
        