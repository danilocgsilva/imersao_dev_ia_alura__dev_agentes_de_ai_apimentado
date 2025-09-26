import os
from suporte.Banco import Banco
from suporte.Comandos.ComandoBase import ComandoBase

class LimparBanco(ComandoBase):
    def executar(self):
        banco = Banco(self._logger)
        resposta = input("ISSO IRÁ REMOVER TODOS OS DADOS QUE VOCÊ JÁ TEM! Tem certeza? Escreva sim para confirmar: ")
        if resposta == "sim":
            self._loginfo("Início da remoção do banco.")
            banco.executar_sql(f"DROP DATABASE IF EXISTS {os.environ.get('NOME_BANCO')}")
            self._loginfo("Banco limpo")
            