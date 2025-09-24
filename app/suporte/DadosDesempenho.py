import time

class DadosDesempenho:
    def __init__(self, llm, temperatura: float, modelo: str, pergunta: str):
        self._llm = llm
        self._temperatura = temperatura
        self._modelo = modelo
        self._pergunta = pergunta
    
    def invoke(self):
        timestamp_antes = time.time_ns()
        resposta = self._llm.invoke(self._pergunta)
        timestamp_depois = time.time_ns()
        diferenca_ms = (timestamp_depois - timestamp_antes) / 1_000_000

        return {
            "resposta": resposta,
            "temperatura": self._temperatura,
            "modelo_utilizado": self._modelo,
            "comando": "ChatGoogleGenerativeAI().invoke(<pergunta>)",
            "timestamp_antes": timestamp_antes / 1000000,
            "timestamp_depois": timestamp_depois / 1000000,
            "diferenca_ms": diferenca_ms
        }