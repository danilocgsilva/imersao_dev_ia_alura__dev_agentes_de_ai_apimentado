from suporte.Comandos.ComandoBase import ComandoBase
from suporte.Rag import Rag

class CarregarDocumentos(ComandoBase):
    def executar(self):
        rag = Rag()
        rag.carrega_documentos()
        print("Verifique os resultados nos logs da aplicação.")
    