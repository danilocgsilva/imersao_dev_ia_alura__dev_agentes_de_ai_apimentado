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
                documento_citacao = self._mostrar_metadata(citacao, "documento")
                pagina_citacao =  self._mostrar_metadata(citacao, "pagina")
                trecho = self._mostrar_metadata(citacao, "trecho")

                print(f" - Documento: {documento_citacao}, Página: {pagina_citacao}")
                print(f"   Trecho: {trecho}")
        print("-----------")

    def _mostrar_metadata(self, citacao, metadata_amigavel: str):
        if metadata_amigavel == "documento":
            return citacao.metadata["source"]
        if metadata_amigavel == "pagina":
            return citacao.metadata["page"]
        if metadata_amigavel == "trecho":
            return citacao.page_content
        raise Exception("Não é esperado essa chave de metadata.")