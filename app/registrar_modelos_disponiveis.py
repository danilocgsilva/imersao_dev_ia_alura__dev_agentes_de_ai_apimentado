from suporte.Banco import Banco
from GoogleApiWrapper import GoogleApiWrapper
from suporte.SupportFactory import SupportFactory

logger = SupportFactory.getLogger()
gaw = GoogleApiWrapper()
banco = Banco()

logger.info("Início da busca dos modelos disponíveis")
modelos = gaw.getModels()
banco.registrar_modelos_disponiveis(modelos)

