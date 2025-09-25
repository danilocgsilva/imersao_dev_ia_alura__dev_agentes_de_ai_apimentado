from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.Comandos.ComandoBase import ComandoBase
from suporte.SupportFactory import SupportFactory

class RegistrarModelosDisponiveis(ComandoBase):
    def executar(self):
        gaw = GoogleApiWrapper(SupportFactory.buscar_chave_google())
        banco = Banco(self._logger)

        self._loginfo("Início da busca dos modelos disponíveis")
        modelos = gaw.getModels()
        self._loginfo("Final da busca dos modelos")
        banco.registrar_modelos_disponiveis(modelos)
        self._loginfo("Colocando o modelo gemini 2.5 flask como primeiro na ordem")
        banco.executar_sql("UPDATE modelos SET ordem = 0 WHERE nome = %s;", ("models/gemini-2.5-flash", ))
        print("Final do registro dos modelos")
    