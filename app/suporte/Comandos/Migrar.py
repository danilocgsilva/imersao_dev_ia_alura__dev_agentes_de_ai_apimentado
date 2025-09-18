from suporte.Banco import Banco
import os
from suporte.SupportFactory import SupportFactory

class Migrar:
    def __init__(self):
        self._logger = SupportFactory.getLogger()
    
    def executar(self):
        banco = Banco(self._logger)

        create_table_script = f"""
        CREATE DATABASE IF NOT EXISTS {os.environ.get('NOME_BANCO')}
        CHARACTER SET utf8mb4 
        COLLATE utf8mb4_unicode_ci;
        """

        self._loginfo("Início da migração do banco.")
        banco.executar_sql(create_table_script)
        banco.nome_banco = os.environ.get('NOME_BANCO')
        banco.executar_sql(self._converter_arquivo_sql_para_string("scripts_migracao/01_tabela_busca_api.sql"))
        banco.executar_sql(self._converter_arquivo_sql_para_string("scripts_migracao/02_tabela_modelos.sql"))
        banco.executar_sql(self._converter_arquivo_sql_para_string("scripts_migracao/03_tabela_propriedades_modelos.sql"))
        self._loginfo("Migração do banco terminada.")
    
    def _converter_arquivo_sql_para_string(self, arquivo: str):
        arquivo_resource = open(arquivo)
        sql_script = arquivo_resource.read()
        arquivo_resource.close()
        return sql_script
    
    def _loginfo(self, mensagem):
        self._logger.info(mensagem)

