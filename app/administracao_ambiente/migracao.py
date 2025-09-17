import sys
sys.path.append("..")
from suporte.Banco import Banco
import os

def converter_arquivo_sql_para_string(arquivo: str):
    arquivo_resource = open(arquivo)
    sql_script = arquivo_resource.read()
    arquivo_resource.close()
    return sql_script

banco = Banco()

create_table_script = f"""
CREATE DATABASE IF NOT EXISTS {os.environ.get('NOME_BANCO')}
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
"""

banco.executar_sql(create_table_script)
banco.nome_banco = os.environ.get('NOME_BANCO')
banco.executar_sql(converter_arquivo_sql_para_string("scripts_migracao/01_tabela_busca_api.sql"))
banco.executar_sql(converter_arquivo_sql_para_string("scripts_migracao/02_tabela_modelos.sql"))
banco.executar_sql(converter_arquivo_sql_para_string("scripts_migracao/03_tabela_propriedades_modelos.sql"))
