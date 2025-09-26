import os
from langchain_community.document_loaders import PyMuPDFLoader
from suporte.ListaDocumentosRag import ListaDocumentosRag
from suporte.AppRootBase import AppRootBase
from suporte.SupportFactory import SupportFactory 
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from google_api.GoogleApiWrapper import GoogleApiWrapper

class Rag(AppRootBase):
    def __init__(self, logger = None):
        if logger == None:
            self._logger = SupportFactory.getLogger()
        else:
            self._logger = logger
        self._documentos_carregados = []
        self._retriever = None
        self._document_chain = None
        
    def setUp(self):
        self.carrega_documentos()
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=SupportFactory.buscar_chave_google()
        )
        vectorstore = FAISS.from_documents(self.buscar_chunks(), embeddings)
        self._retriever = vectorstore.as_retriever(
            search_type="similarity_score_threshold", 
            search_kwargs={
                "score_threshold": 0.3,
                "k": 4
            }
        )
        prompt_rag = ChatPromptTemplate.from_messages([
            ("system",
            "Você é um Assistente de Políticas Internas (RH/IT) da empresa Carraro Desenvolvimento. "
            "Responda SOMENTE com base no contexto fornecido. "
            "Se não houver base suficiente, responda apenas 'Não sei'."),

            ("human", "Pergunta: {input}\n\nContexto:\n{context}")
        ])
        
        google_api_wrapper = GoogleApiWrapper(SupportFactory.buscar_chave_google())
        self._document_chain = create_stuff_documents_chain(
            google_api_wrapper.getLLM(),
            prompt_rag
        )
            
    def buscar_chunks(
        self, 
        chunk_size: int = 300, 
        chunk_overlap: int = 30
    ):
        splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = splitter.split_documents(self._documentos_carregados)
        return chunks

        
    def perguntar_politica_rag(self, pergunta: str) -> dict:
        documentos_relacionados = self._retriever.invoke(pergunta)
        if not documentos_relacionados:
            return {
                "answer": "Não sei",
                "citacoes": [],
                "contexto_encontrado": False
            }
        answer = self._document_chain.invoke({
            "input": pergunta,
            "context": documentos_relacionados
        })
        txt = (answer or "").strip()
        if txt.rstrip(".!?") == "Não sei":
            return {
                "answer": "Não sei",
                "citacoes": [],
                "contexto_encontrado": False
            }
        return {
            "answer": txt,
            "citacoes": documentos_relacionados,
            "contexto_encontrado": True
        }
        
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