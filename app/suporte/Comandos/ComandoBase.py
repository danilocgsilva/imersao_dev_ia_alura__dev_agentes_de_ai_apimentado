from suporte.SupportFactory import SupportFactory

class ComandoBase:
    def __init__(self):
        self._logger = SupportFactory.getLogger()

    def _loginfo(self, mensagem):
        self._logger.info(mensagem)