from suporte.Banco import Banco
import os
from suporte.Comandos.ComandoBase import ComandoBase

class Migrar(ComandoBase):
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
        
        self._executar_sql_com_stdout(banco, "scripts_migracao/01_tabela_busca_api.sql")
        self._executar_sql_com_stdout(banco, "scripts_migracao/02_tabela_modelos.sql")
        self._executar_sql_com_stdout(banco, "scripts_migracao/03_tabela_propriedades_modelos.sql")
        self._executar_sql_com_stdout(banco, "scripts_migracao/04_tabela_perguntas.sql")
        self._executar_sql_com_stdout(banco, "scripts_migracao/05_tabela_respostas.sql")
        self._executar_sql_com_stdout(banco, "scripts_migracao/06_tabela_perguntas_modelo.sql")
        self._executar_sql_com_stdout(banco, "scripts_migracao/07_adicao_perguntas_modelo.sql")
        
        self._loginfo("Migração do banco terminada.")
    
    def _converter_arquivo_sql_para_string(self, arquivo: str):
        arquivo_resource = open(arquivo)
        sql_script = arquivo_resource.read()
        arquivo_resource.close()
        return sql_script
    
    def _executar_sql_com_stdout(self, banco: Banco, caminho_arquivo):
        query = self._converter_arquivo_sql_para_string(caminho_arquivo)
        print("Executando query:")
        print(query)
        banco.executar_sql(query)
    