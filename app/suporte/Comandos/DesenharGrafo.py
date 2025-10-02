from suporte.Comandos.ComandoBase import ComandoBase
from suporte.SupportFactory import SupportFactory
from datetime import datetime
import os
from suporte.Grafo import Grafo

class DesenharGrafo(ComandoBase):
    def __init__(self):
        self._logger = SupportFactory.getLogger()
    
    def executar(self):
        grafo = Grafo().buscar()
        resultados = self._salvar_imagem(grafo)
        print(f"Finalizado o desenho do grafo: {resultados['caminho']}")

    def _salvar_imagem(self, grafo):
        caminho_base: str = "/app/grafos"
        string_data_amigavel = self._gerar_string_data_amigavel()
        nome_arquivo = f"grafo_{string_data_amigavel}.png"
        nome_arquivo_caminho_cheio = os.path.join(caminho_base, nome_arquivo)
        bytes_grafico = grafo.get_graph().draw_mermaid_png()
        with open(nome_arquivo_caminho_cheio, "wb") as f:
            f.write(bytes_grafico)
        return {
            "nome_arquivo": nome_arquivo,
            "caminho": nome_arquivo_caminho_cheio
        }
        
    def _gerar_string_data_amigavel(self) -> str:
        return datetime.now().strftime("%Y%m%d_%Hh%Mm%Ss")
        
