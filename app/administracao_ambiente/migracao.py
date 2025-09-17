import sys
sys.path.append("..")
from suporte.banco import executar_sql
import os

def converter_arquivo_sql_para_string(arquivo: str):
    sql_script = open(arquivo).read()
    return sql_script

sql_string = f"""
CREATE DATABASE IF NOT EXISTS {os.environ.get('NOME_BANCO')}
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
"""

executar_sql(sql_string)
executar_sql(converter_arquivo_sql_para_string("tabela_modelos.sql"))

