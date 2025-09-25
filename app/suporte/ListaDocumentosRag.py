import os
from suporte.AppRootBase import AppRootBase

class ListaDocumentosRag(AppRootBase):
    @property
    def documentos(self):
        rag_path = os.path.join(self.app_root, 'flask_app', 'documentos_rag', 'fixos')
        return os.listdir(rag_path)
    