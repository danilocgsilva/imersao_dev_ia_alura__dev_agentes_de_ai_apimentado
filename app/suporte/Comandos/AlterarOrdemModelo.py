from suporte.SupportFactory import SupportFactory
from suporte.Banco import Banco

class AlterarOrdemModelo:
    def __init__(self):
        self._logger = SupportFactory.getLogger()
        self._modelo = ""
        self._ordem = ""
        
    def executar(self):
        if self._modelo == "" or self._ordem == "":
            mensagem = "Modelo ou ordem não informado. Ambos são parâmetro obrigatórios."
            self._logerror(mensagem)
            raise Exception(mensagem)
        banco = Banco(self._logger)
        banco.alterar_ordem_modelo(self._modelo, self._ordem)
        
    @property
    def modelo(self) -> str:
        return self._modelo
    
    @property
    def ordem(self) -> str:
        return self._ordem
    
    @modelo.setter
    def modelo(self, modelo: str):
        self._modelo = modelo
        
    @ordem.setter
    def ordem(self, ordem: str):
        self._ordem = ordem
        
    def _loginfo(self, mensagem):
        if self._logger:
            self._logger.info(mensagem)

    def _logerror(self, mensagem):
        if self._logger:
            self._logger.error(mensagem)