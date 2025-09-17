import mysql.connector
import os
from GoogleApiWrapper import GoogleApiWrapper
import pickle
import base64

class Banco:
    def __init__(self):
        self._nome_banco = None
    
    @property
    def nome_banco(self):
        return self._nome_banco
    
    @nome_banco.setter
    def nome_banco(self, nome_banco: str):
        self._nome_banco = nome_banco
        
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
            return results
        except mysql.connector.Error as err:
            print(f"Error connecting to database or executing query: {err}")
        finally:
            if mydb and mydb.is_connected():
                mydb.commit()
                mycursor.close()
                mydb.close()
    
    def registrar_modelos_disponiveis(self, modelos: list):
        
        self.registrar_request_de_busca_modelos_disponiveis(modelos)
        
        for modelo in modelos:
            print("-----")
            for property in dir(modelo):
                value = getattr(modelo, property)
                value_type = type(value).__name__
                
                is_method = value_type == "method"
                is_none_type = value_type == "NoneType"
                is_builtin_function_or_method = value_type == "builtin_function_or_method"
                is_method_wrapper = value_type == "method-wrapper"
                is_tuple = value_type == "tuple"
                is_dict = value_type == "dict"
                is_data_class_params = value_type == "_DataclassParams"
                is_type = value_type == "type"
                is_list = value_type == "list"
                
                if not is_none_type \
                    and not is_builtin_function_or_method \
                    and not is_method \
                    and not is_method_wrapper \
                    and not is_tuple \
                    and not is_dict \
                    and not is_data_class_params \
                    and not is_type \
                    and not is_list:
                    print(f"   - {property}, {value_type} ,{value}")
                    
    def registrar_request_de_busca_modelos_disponiveis(self, modelos):
        modelos_serializados = pickle.dumps(modelos)
        modelos_serializados_base64 = base64.b64encode(modelos_serializados).decode('utf-8')
        self.nome_banco = os.environ.get("NOME_BANCO")
        self.executar_sql(f"INSERT INTO busca_api (comando, retorno_serializado) VALUES (%s, %s);", ('GoogleApiWrapper().getModels()', modelos_serializados_base64,))
        