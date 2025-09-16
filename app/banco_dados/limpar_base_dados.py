from funcoes_banco import executar_sql
import os

resposta = input("ISSO IRÁ REMOVER TODOS OS DADOS QUE VOCÊ JÁ TEM! Tem certeza? Escreva sim para confirmar: ")
if resposta == "sim":
    executar_sql(f"DROP DATABASE {os.environ.get('NOME_BANCO')}")
