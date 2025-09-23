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
        logger.info("Coloando o modelo gemini 2.5 flask como primeiro na ordem")
        banco.executar_sql("UPDATE modelos SET ordem = 0 WHERE nome = %s;", ("models/gemini-2.5-flash", ))
        print("Final do registro dos modelos")
    