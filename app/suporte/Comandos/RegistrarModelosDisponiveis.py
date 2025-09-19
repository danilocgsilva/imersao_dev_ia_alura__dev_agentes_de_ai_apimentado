from suporte.Banco import Banco
from google_api.GoogleApiWrapper import GoogleApiWrapper
from suporte.SupportFactory import SupportFactory
import os

class RegistrarModelosDisponiveis:
    def executar(self):
        logger = SupportFactory.getLogger()
        gaw = GoogleApiWrapper(SupportFactory.buscar_chave_google())
        banco = Banco(logger)

        logger.info("Início da busca dos modelos disponíveis")
        modelos = gaw.getModels()
        logger.info("Final da busca dos modelos")
        banco.registrar_modelos_disponiveis(modelos)
        print("Final do registro dos modelos")
    