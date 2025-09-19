from suporte.SupportFactory import SupportFactory
from suporte.Banco import Banco
from suporte.Comandos.LimparBanco import LimparBanco
from suporte.Comandos.Migrar import Migrar

class RenovarBanco:
    def executar(self):
        LimparBanco().executar()
        Migrar().executar()
        
    def _debug(self, message):
        self._logger.info(message)