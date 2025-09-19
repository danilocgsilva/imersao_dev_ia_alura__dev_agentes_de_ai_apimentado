import pickle
import base64

class Utilidades:
    @staticmethod
    def serializar(conteudo: str) -> str:
        serializacao = pickle.dumps(conteudo)
        serializacao_base64 = base64.b64encode(serializacao).decode('utf-8')
        return serializacao_base64