from suporte.Comandos.ComandoBase import ComandoBase
from suporte.Rag import Rag

class VerChunksDocumentos(ComandoBase):
    def executar(
        self,
        tamanho_chunk = 300,
        chunk_overlap = 30,
        apenas_page_content = False
    ):
        rag = Rag()
        rag.carrega_documentos()
        chunks = rag.buscar_chunks(tamanho_chunk, chunk_overlap)
        
        if apenas_page_content:
            chunks = list(map(lambda x: x.page_content, chunks))
        
        quantidade_chunks = 1
        for chunk in chunks:
            print(f"---- chunk {quantidade_chunks} -------------")
            print(chunk)
            quantidade_chunks += 1
        print("----")
        print(f"Quantidade de chunks: {len(chunks)}")
        
    