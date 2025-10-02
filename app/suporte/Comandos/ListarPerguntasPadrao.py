from suporte.Banco import Banco
from suporte.Comandos.ComandoBase import ComandoBase

class ListarPerguntasPadrao(ComandoBase):
    def executar(self):
        banco = Banco(self._logger)
        perguntas = banco.listar_perguntas_modelo()
        for pergunta in perguntas:
            print(f"{pergunta[0]} - {pergunta[1]}")
