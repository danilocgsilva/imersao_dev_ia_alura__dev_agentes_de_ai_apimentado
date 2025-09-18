from suporte.Banco import Banco
from GoogleApiWrapper import GoogleApiWrapper
from suporte.SupportFactory import SupportFactory

class RegistrarModelosDisponiveis:
    def execute(self):
        logger = SupportFactory.getLogger()
        gaw = GoogleApiWrapper()
        banco = Banco(logger)

        logger.info("Início da busca dos modelos disponíveis")
        modelos = gaw.getModels()
        logger.info("Final da busca dos modelos")
        banco.registrar_modelos_disponiveis(modelos)
    