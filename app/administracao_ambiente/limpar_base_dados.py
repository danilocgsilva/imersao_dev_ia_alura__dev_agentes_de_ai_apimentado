import sys
import os
sys.path.append("..")
from suporte.Banco import Banco

banco = Banco()

resposta = input("ISSO IRÁ REMOVER TODOS OS DADOS QUE VOCÊ JÁ TEM! Tem certeza? Escreva sim para confirmar: ")
if resposta == "sim":
    banco.executar_sql(f"DROP DATABASE {os.environ.get('NOME_BANCO')}")
