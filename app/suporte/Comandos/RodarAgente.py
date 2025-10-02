from suporte.Comandos.ComandoBase import ComandoBase
from suporte.Grafo import Grafo

class RodarAgente(ComandoBase):
    def __init__(self):
        self._pergunta = None

    @property
    def pergunta(self):
        self._pergunta

    @pergunta.setter
    def pergunta(self, pergunta):
        self._pergunta = pergunta

    def executar(self):
        grafo = Grafo().buscar()
        resposta_final = grafo.invoke({"pergunta": self._pergunta})
        triagem = resposta_final.get("triagem", {})
        print(f"PERGUNTA: {self._pergunta}")
        print(f"DECISÃO: {triagem.get('decisao')} | URGÊNCIA: {triagem.get('urgencia')} | AÇÃO FINAL: {triagem.get('acao_final')}")
        print(f"RESPOSTA: {resposta_final.get('resposta')}")
        if resposta_final.get("citacoes"):
            print("CITAÇÕES")
            for citacao in resposta_final.get("citacoes"):
                print(f" - Documento: {citacao.get('documento')}, Página: {citacao.get('pagina')}")
                print(f"   Trecho: {citacao.get('trecho')}")
        print("-----------")
