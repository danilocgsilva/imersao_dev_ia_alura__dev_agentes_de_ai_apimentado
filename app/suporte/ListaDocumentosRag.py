import os
from suporte.AppRootBase import AppRootBase
from suporte.Banco import Banco

class ListaDocumentosRag(AppRootBase):
    def __init__(self):
        self._banco = Banco()
        
    @property
    def documentos(self):
        arquivos_filtrados = []
        
        rag_path = os.path.join(
            self.app_root, 'flask_app', 'documentos_rag', 'fixos'
        )
        dados_arquivos_bancos = self._banco.buscar_configuracoes()
        arquivos_diretorio_fixo = os.listdir(rag_path)
        for arquivo_dado in dados_arquivos_bancos:
            if arquivo_dado[0] in arquivos_diretorio_fixo and arquivo_dado[1] == 1:
                arquivos_filtrados.append(
                    os.path.join('fixos', arquivo_dado[0])
                )
                
        rag_path_dinamicos = os.path.join(self.app_root, 'flask_app', 'documentos_rag', 'dinamicos')
        arquivos_diretorio_dinamicos_flat = os.listdir(
            rag_path_dinamicos
        )
        
        arquivos_diretorio_dinamicos = list(map(lambda x : os.path.join('dinamicos', x), arquivos_diretorio_dinamicos_flat))
        
        return arquivos_filtrados + arquivos_diretorio_dinamicos
    