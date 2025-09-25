from suporte.Comandos.ComandoBase import ComandoBase
from suporte.Rag import Rag

class VerChunksDocumentos(ComandoBase):
    def executar(self):
        rag = Rag()
        rag.carrega_documentos()
        print(rag.buscar_chunks())
        
    