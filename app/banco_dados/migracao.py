from funcoes_banco import executar_sql
import os

sql_string = f"""
CREATE DATABASE {os.environ.get('NOME_BANCO')}
CHARACTER SET utf8mb4 
COLLATE utf8mb4_unicode_ci;
"""


executar_sql(sql_string)
