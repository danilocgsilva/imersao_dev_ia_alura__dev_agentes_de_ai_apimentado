from suporte.Banco import Banco
from GoogleApiWrapper import GoogleApiWrapper

gaw = GoogleApiWrapper()
banco = Banco()

modelos = gaw.getModels()
banco.registrar_modelos_disponiveis(modelos)

