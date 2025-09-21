import mysql.connector
import os
from .Utilidades import Utilidades
from .SupportFactory import SupportFactory

class Banco:
    def __init__(self, logger = None):
        self._nome_banco = None
        self._ultimo_id_inserido_banco = None
        if logger == None:
            self._logger = SupportFactory.getLogger()
        else:
            self._logger = logger
    
    @property
    def nome_banco(self):
        return self._nome_banco
    
    @nome_banco.setter
    def nome_banco(self, nome_banco: str):
        self._nome_banco = nome_banco
        
    @property
    def ultimo_id_inserido(self):
        return self._ultimo_id_inserido_banco
        
    def executar_sql(self, sql_script: str, scaping_replacements: tuple = ()):
        try:
            mydb = mysql.connector.connect(
                host=os.environ.get("HOST_BANCO"),
                user=os.environ.get("USUARIO_BANCO"),
                password=os.environ.get("SENHA_BANCO")
            )
            mycursor = mydb.cursor()
            if self.nome_banco:
                mycursor.execute(f"USE {self.nome_banco}")
            mycursor.execute(sql_script, scaping_replacements)
            results = mycursor.fetchall()
            self._ultimo_id_inserido_banco = mycursor.lastrowid
            return results
        except mysql.connector.Error as err:
            mensagem_erro = f"Error connecting to database or executing query: {err}"
            self._logger.error(mensagem_erro)
            print(mensagem_erro)
        finally:
            if mydb and mydb.is_connected():
                mydb.commit()
                mycursor.close()
                mydb.close()
    
    def registrar_modelos_disponiveis(self, modelos: list):
        quantidade_modelos_encontrados = str(len(modelos))
        self._loginfo(f"Foram encontrados {quantidade_modelos_encontrados} modelos")
        self.registrar_request_de_busca_modelos_disponiveis(modelos)
        self._loginfo("Resultados da busca da api registrados em banco.")
        
        id_registro_request = self.ultimo_id_inserido
        
        loop_modelos = 1
        for modelo in modelos:
            self._loginfo(f"Modelo {loop_modelos} de {quantidade_modelos_encontrados} modelos.")
            self.salvar_modelo(modelo, id_registro_request)
            id_modelo_iteracao = self.ultimo_id_inserido
            self.registrar_metadados_modelo(modelo, id_modelo_iteracao)
            self._loginfo(f"Modelo {modelo.name} registrado em banco")
            loop_modelos += 1
            
    def registrar_request_de_busca_modelos_disponiveis(self, modelos):
        self.nome_banco = os.environ.get("NOME_BANCO")
        modelos_serializados_base64 = Utilidades.serializar(modelos)
        self.executar_sql(f"INSERT INTO busca_api (comando, retorno_serializado) VALUES (%s, %s);", ('GoogleApiWrapper().getModels()', modelos_serializados_base64,))
        
    def registrar_request(self, conteudo, comando):
        self.nome_banco = os.environ.get("NOME_BANCO")
        conteudo_serializado = Utilidades.serializar(conteudo)
        self.executar_sql(f"INSERT INTO busca_api (comando, retorno_serializado) VALUES (%s, %s);", (comando, conteudo_serializado,))
        
    def salvar_modelo(self, modelo, id_registro_request: int):
        self.nome_banco = os.environ.get("NOME_BANCO")
        self.executar_sql("INSERT INTO modelos (nome, ordem, busca_id) VALUES (%s, %s, %s)", (modelo.name, 1, id_registro_request))
        
    def listar_modelos_disponiveis(self):
        self.nome_banco = os.environ.get("NOME_BANCO")
        modelos_disponiveis = self.executar_sql("SELECT id, nome, ordem, busca_id FROM modelos ORDER BY ordem ASC, nome ASC;")
        return modelos_disponiveis

    def registrar_metadados_modelo(self, modelo, id_modelo):
        for property in dir(modelo):
            value = getattr(modelo, property)
            value_type = type(value).__name__
            
            is_str = value_type == "str"
            is_int = value_type == "int"
            is_float = value_type == "float"
            is_list = value_type == "list"
            
            if is_str or is_int or is_float:
                self.executar_sql("INSERT INTO modelos_meta_dados (campo, tipo_valor, valor, modelo_id) VALUES (%s, %s, %s, %s);", (property, value_type, value, id_modelo))
            if is_list:
                for entry in value:
                    self.executar_sql("INSERT INTO modelos_meta_dados (campo, tipo_valor, valor, modelo_id) VALUES (%s, %s, %s, %s);", (property, value_type, entry, id_modelo))

    def registrar_pergunta(self, pergunta):
        self.nome_banco = os.environ.get("NOME_BANCO")
        self.executar_sql("INSERT INTO perguntas (pergunta) VALUES (%s)", (pergunta, ))
        
    def registrar_resposta(
        self, 
        resposta: str,
        id_pergunta: int,
        resposta_cheia,
        temperatura: int,
        modelo_utilizado: str,
        timestamp_antes: float,
        timestamp_depois: float,
        diferenca_ms: float
    ):
        self.nome_banco = os.environ.get("NOME_BANCO")
        resposta_serializada = Utilidades.serializar(resposta_cheia)
        query_insert = """
            INSERT INTO respostas (
                resposta, 
                pergunta_id, 
                resposta_api_total, 
                temperatura, 
                modelo_utilizado,
                data_inicio_pergunta_milissegundos,
                data_final_pergunta_milissegundos,
                diferenca_milissegundos
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.executar_sql(
            query_insert, 
            (resposta, id_pergunta, resposta_serializada, temperatura, modelo_utilizado, timestamp_antes, timestamp_depois, diferenca_ms)
        )
                    
    def _loginfo(self, mensagem):
        if self._logger:
            self._logger.info(mensagem)
