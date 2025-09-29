import os
from suporte.AppRootBase import AppRootBase
from suporte.Banco import Banco

class ListaDocumentosRag(AppRootBase):
    def __init__(self):
        self._banco = Banco()
        
    @property
    def documentos(self):
        rag_path = os.path.join(self.app_root, 'flask_app', 'documentos_rag', 'fixos')
        dados_arquivos_bancos = self._banco.buscar_configuracoes()
        # arquivos_bancos = list(map(lambda x : x[0], dados_arquivos_bancos))
        arquivos_diretorio = os.listdir(rag_path)
        arquivos_filtrados = []
        for arquivo_dado in dados_arquivos_bancos:
            if arquivo_dado[0] in arquivos_diretorio and arquivo_dado[1] == 1:
                arquivos_filtrados.append(arquivo_dado[0])
        
        return arquivos_filtrados
    