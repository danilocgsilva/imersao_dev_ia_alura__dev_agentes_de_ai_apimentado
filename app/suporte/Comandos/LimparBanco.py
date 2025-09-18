import os
from suporte.Banco import Banco
from suporte.SupportFactory import SupportFactory

class LimparBanco:
    def __init__(self):
        self._logger = SupportFactory.getLogger()
        
    def executar(self):
        banco = Banco(self._logger)
        resposta = input("ISSO IRÁ REMOVER TODOS OS DADOS QUE VOCÊ JÁ TEM! Tem certeza? Escreva sim para confirmar: ")
        if resposta == "sim":
            self._debug("Início da remoção do banco.")
            banco.executar_sql(f"DROP DATABASE IF EXISTS {os.environ.get('NOME_BANCO')}")
            self._debug("Banco limpo")
            
    def _debug(self, message):
        self._logger.info(message)