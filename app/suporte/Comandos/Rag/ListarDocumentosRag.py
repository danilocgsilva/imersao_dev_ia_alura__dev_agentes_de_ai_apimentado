from suporte.Comandos.ComandoBase import ComandoBase
from suporte.ListaDocumentosRag import ListaDocumentosRag
from suporte.Rag import Rag

class ListarDocumentosRag(ComandoBase):
    def executar(self):
        lista_documentos = ListaDocumentosRag().documentos
        
        for documento in lista_documentos:
            print(documento)
