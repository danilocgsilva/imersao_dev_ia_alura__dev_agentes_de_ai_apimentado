from getLLM import getLLM

llm = getLLM()
# modelos_disponiveis = llm.list_models()
resposta_teste = llm.invoke("Qual a capital da França?")
print(resposta_teste)
