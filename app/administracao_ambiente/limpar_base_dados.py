import sys
import os
sys.path.append("..")
from suporte.banco import executar_sql

resposta = input("ISSO IRÁ REMOVER TODOS OS DADOS QUE VOCÊ JÁ TEM! Tem certeza? Escreva sim para confirmar: ")
if resposta == "sim":
    executar_sql(f"DROP DATABASE {os.environ.get('NOME_BANCO')}")
