from langchain_community.document_loaders import PyMuPDFLoader
from suporte.ListaDocumentosRag import ListaDocumentosRag
from suporte.AppRootBase import AppRootBase
from suporte.SupportFactory import SupportFactory 
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter

class Rag(AppRootBase):
    def __init__(self, logger = None):
        if logger == None:
            self._logger = SupportFactory.getLogger()
        else:
            self._logger = logger
        self._documentos_carregados = []
            
    def buscar_chunks(
        self, 
        chunk_size: int = 300, 
        chunk_overlap: int = 30
    ):
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = splitter.split_documents(self._documentos_carregados)
        return chunks
    
    def carrega_documentos(self):
        lista_documentos_rag = ListaDocumentosRag().documentos
        for documento_nome in lista_documentos_rag:
            try:
                loader = PyMuPDFLoader(os.path.join(self.app_root, 'flask_app', 'documentos_rag', 'fixos', documento_nome))
                self._documentos_carregados.extend(loader.load())
                self._logger.info(f"Documento {documento_nome} carregado com sucesso.")
            except Exception as e:
                self._logger.info(f"Erro ao carregar o documento {documento_nome}: {e}")
        self._logger.info(f"Documentos carregados: {len(self._documentos_carregados)}.")
        
    @property
    def documentos_carregados(self):
        return self._documentos_carregados